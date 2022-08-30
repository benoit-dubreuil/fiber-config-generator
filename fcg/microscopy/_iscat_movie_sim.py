import csv
import json
import pickle
import pathlib

import imageio
import numpy as np
import tqdm
import scipy.signal
import skimage.util


# TODO : Migrate imageio v2 API to v3 API :
#  See https://imageio.readthedocs.io/en/stable/reference/userapi.html#migrating-to-the-v3-api

# Moving Acquisition simulation
class Microscope3dAcquisitionSimulator:
    """Generate a synthetic [iScat](https://en.wikipedia.org/wiki/Interferometric_scattering_microscopy) movie from a
    set of tracks.

    **Syntax**:

    .. code-block:: python

        movie_simulator = iscat_movie(tracks)
        movie_simulator.run()

    **Authors**:

    | Joël Lefebvre (lefebvre.joel@uqam.ca)
    | Department of Computer Sciences
    | Université du Québec a Montréal (UQAM)
    | 201, Av. du Président-Kennedy, Montréal (Qc), Canada (H3C 3P8)

    Parameters
    ----------
    tracks : dict or CSV filename
        A dictionary or a CSV filename containing the set of tracks to simulate. The dictionary must include the keys
        `x`, `y`, `t` and `id`
    resolution : float
        Spatial resolution [m/px]
    dt : float
        Temporal resolution  [frame/sec]
    contrast : float
        Contrast between the simulated particle and the background (Contrast = particle intensity - background
        intensity)
    background : float
        Background intensity between 0 and 1
    noise_gaussian : float
        Gaussian noise variance
    noise_poisson : bool
        If True, Poisson noise will be added.
    ratio : str
        Aspect ratio of the simulated movie. Available ("square"). If none is given,
        the aspect ratio will be inferred from the tracks position.

    """

    # Notes
    # TODO: Add PSF & Object shape inputs (instead of only psf)
    # TODO: Add z-phase jitter for the PSF instead of using a fixed plane
    # TODO: Load a simulation parameters file instead of passing everything in the command line
    # TODO: Use input size as alternative
    # TODO: link tqdm with logging
    # TODO: Create a python wrapper for the ImageJ plugin 'DeconvolutionLab2' to generate PSF in the script?
    # TODO: Background noise with different statistics (similar to transcient particles)
    def __init__(
        self,
        tracks=None,
        resolution=1.0,
        dt=1,
        contrast=5,
        background=0.3,
        noise_gaussian=0.15,
        noise_poisson=True,
        ratio="square",
    ):
        # Prepare the simulator
        self.resolution = resolution
        self.contrast = contrast  # Contrast between the simulated particle and the background
        self.background = background  # Background intensity
        self.noise_gaussian = noise_gaussian  # Gaussian noise variance
        self.noise_poisson = noise_poisson  # Poisson noise variance
        self.dt = dt  # Temporal resolution
        self.ratio = ratio
        self.initialized = False

        if isinstance(tracks, dict):
            self.tracks = tracks
        elif isinstance(tracks, str) or isinstance(tracks, pathlib.Path):
            self.load_tracks(tracks)

    def initialize(self):
        """Initialize the simulator"""
        assert hasattr(self, "tracks"), "You must load a tracks file or set a tracks dict first"
        self.n_spots = len(self.tracks["x"])

        # Get the number of frames
        self.tmin = 0
        self.tmax = np.max(self.tracks["t"])
        self.n_frames = int((self.tmax - self.tmin) / self.dt) + 1

        # Get the movie shape
        self.xmin = np.min(self.tracks["x"])
        self.ymin = np.min(self.tracks["y"])
        self.xmax = np.max(self.tracks["x"])
        self.ymax = np.max(self.tracks["y"])
        if self.ratio == "square":
            self.xmin = min(self.xmin, self.ymin)
            self.ymin = min(self.xmin, self.ymin)
            self.xmax = max(self.xmax, self.ymax)
            self.ymax = max(self.xmax, self.ymax)
        else:
            print(f"Unknown ratio: {self.ratio}")

        # Initialize the simulation grid
        x = np.linspace(self.xmin, self.xmax, int((self.xmax - self.xmin) / self.resolution))
        y = np.linspace(self.ymin, self.ymax, int((self.ymax - self.ymin) / self.resolution))
        self.nx = len(x) + 1
        self.ny = len(y) + 1

        self.initialized = True

        print(" - - - - - - - - ")
        print(self.tmax)
        print(len(x))
        print("self.xmin", self.xmin)
        print("self.ymin", self.ymin)
        print("self.xmax", self.xmax)

        print(f"Movie shape will be: ({self.nx}, {self.ny}) with ({self.n_frames}) frames")

    def get_estimated_size(self):
        """Return the estimated movie size in MB"""
        return self.nx * self.ny * self.n_frames * 8 / 1000 ** 2  # Using double precision float (float64)

    def run(self, reinitialize=False):
        """Run the movie simulation
        Parameters
        ----------
        reinitialize: bool
            If `True`, the simulator will be reinitialized.
        """
        if reinitialize or not (self.initialized):
            self.initialize()

        # Create the movie array
        print("Creating an empty movie")
        movie = np.ones((self.n_frames, self.nx, self.ny), dtype=np.float64) * self.background

        # Add Gaussian noise to the background
        if self.noise_gaussian is not None:
            print("Adding gaussian noise to the background")
            movie = skimage.util.random_noise(movie, mode="gaussian", var=self.noise_gaussian)

        # Populate the tracks
        for this_spot in tqdm.tqdm(range(self.n_spots), "Adding tracks"):
            mx = int(np.round((self.tracks["x"][this_spot] - self.xmin) / self.resolution))
            my = int(np.round((self.tracks["y"][this_spot] - self.ymin) / self.resolution))
            mt = int(self.tracks["t"][this_spot] / self.dt)
            if isinstance(mx, list):
                for x, y, t in zip(mx, my, mt):
                    if (0 <= mx < self.nx) and (0 <= my < self.ny):
                        movie[t, x, y] += self.contrast
            else:
                if (0 <= mx < self.nx) and (0 <= my < self.ny):
                    movie[mt, mx, my] += self.contrast

        # Convolve by PSF if provided
        if hasattr(self, "psf_2d"):
            px, py = self.psf_2d.shape
            movie = np.pad(movie, ((0, 0), (px // 2, px // 2), (py // 2, py // 2)), mode="reflect")

            # Apply convolution
            for i in tqdm.tqdm(range(self.n_frames), desc="Convolving with PSF"):
                movie[i, ...] = scipy.signal.fftconvolve(movie[i, ...], self.psf_2d, mode="same")

            # Unpad
            movie = movie[:, px // 2 : px // 2 + self.nx, py // 2 : py // 2 + self.ny]

        # Add Poisson noise
        if self.noise_poisson:
            print("Adding Poisson noise")
            movie = skimage.util.random_noise(movie, mode="poisson", clip=False)
            movie[movie < 0] = 0

        self.movie = movie
        print("Movie generation is done.")

    def save(self, filename):
        """Save the simulated movie.
        Parameters
        ----------
        filename : str
            Output volume filename. Must be a volume format supported by `imageio.volwrite`
        Note
        ----
        The volume will be converted to single precision float (`numpy.float32`)
        """
        assert hasattr(self, "movie"), "You must first run the simulation"
        imageio.volwrite(filename, self.movie.astype(np.float32))

    def load_tracks(
        self, filename, field_x="x", field_y="y", field_t="t", field_id="id", file_format=None
    ):  # TODO: Load other tracks format
        """Load the tracks from a csv file.

        Parameters
        ----------
        filename : str
            Path to a csv filename
        field_x : str
            Column name in the CSV corresponding to the tracks X positions.
        field_y : str
            Column name in the CSV corresponding to the tracks Y positions.
        field_t : str
            Column name in the CSV corresponding to the tracks time.
        field_id : str
            Column name in the CSV corresponding to the tracks ID.
        file_format : str
            Specify the file format (available are cvs, json, pcl). If none is given, it will be inferred from the
            filename
        """
        tracks = {"x": [], "y": [], "t": [], "id": []}
        if pathlib.Path(filename).suffix == ".csv" or file_format == "csv":
            # Load the csv file
            with open(filename) as csvfile:
                #  Detect the csv format
                dialect = csv.Sniffer().sniff(csvfile.read())

                #  Create a reader
                csvfile.seek(0)
                reader = csv.reader(csvfile, dialect)

                for i, row in enumerate(reader):
                    if i == 0:
                        column_names = row
                    else:
                        tracks["x"].append(float(row[column_names.index(field_x)]))
                        tracks["y"].append(float(row[column_names.index(field_y)]))
                        tracks["t"].append(float(row[column_names.index(field_t)]))
                        tracks["id"].append(int(row[column_names.index(field_id)]))
        elif pathlib.Path(filename).suffix == ".json" or file_format == "json":
            with open(filename) as f:
                content = json.load(f)
            tracks["x"] = content[field_x]
            tracks["y"] = content[field_y]
            tracks["t"] = content[field_t]
            tracks["id"] = content[field_id]

        elif pathlib.Path(filename).suffix == ".pcl" or file_format == "pcl":
            with open(filename, "rb") as f:
                content = pickle.load(f)
            tracks["x"] = content[field_x]
            tracks["y"] = content[field_y]
            tracks["t"] = content[field_t]
            tracks["id"] = content[field_id]

        self.tracks = tracks

    def load_psf(self, filename):
        """Load a Point-Spread Function (PSF) from a file
        Parameters
        ----------
        filename: str
            Input volume filename. Must be a volume format supported by `imageio.volwrite`
        Note
        ----
        Only the middle slice along the first dimension will be used
        .. code-block:: python
            psf = psf[int(psf.shape[0]/2), ...]
        """
        psf = imageio.volread(filename).squeeze()
        psf_2d = psf[int(psf.shape[0] / 2), ...].squeeze()
        psf_2d = psf_2d / psf_2d.sum()
        self.psf_2d = psf_2d
