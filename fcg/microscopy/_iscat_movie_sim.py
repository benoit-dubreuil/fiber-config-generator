import pathlib

import imageio
import numpy as np
import numpy.typing as npt
import scipy.signal
import skimage.util
import tqdm

from ._psf import load_psf
from ._tract import Tracts, load_tracts

# TODO : Migrate imageio v2 API to v3 API :
#  See https://imageio.readthedocs.io/en/stable/reference/userapi.html#migrating-to-the-v3-api

# Moving Acquisition simulation
#
# @formatter:off
# noqa Adapted from https://github.com/Eggeling-Lab-Microscope-Software/TRAIT2D/blob/c0e78a61f58bd12f5e2b63e99dbc5a130ef740bb/trait2d/simulators.py#L412
# @formatter:on
class MovieAcquisitionSimulator:
    """Generate a synthetic iScat_ movie from a set of tracts.

    **Syntax**:

    .. code-block:: python

        movie_simulator = MovieAcquisitionSimulator(args...)
        movie_simulator.run()

    **Authors**:

    | Joël Lefebvre (lefebvre.joel@uqam.ca)
    | Department of Computer Sciences
    | Université du Québec a Montréal (UQAM)
    | 201, Av. du Président-Kennedy, Montréal (Qc), Canada (H3C 3P8)

    Attributes
    ----------
    tracts
        Tracts to simulate.
    psf_2d
        Point-Spread Function (PSF)
    resolution
        Spatial resolution [m/px]
    dt
        Temporal resolution [frame/sec]
    contrast
        Contrast between the simulated particle and the background (Contrast = particle intensity - background
        intensity)
    background
        Background intensity between 0 and 1
    noise_gaussian
        Gaussian noise variance
    noise_poisson
        If True, Poisson noise will be added.
    ratio
        Aspect ratio of the simulated movie. Available ("square"). If none is given,
        the aspect ratio will be inferred from the tracts position.

    .. _iScat: https://en.wikipedia.org/wiki/Interferometric_scattering_microscopy

    """

    tracts: Tracts
    psf_2d: npt.NDArray | None
    resolution: float
    dt: float
    contrast: float
    background: float
    noise_gaussian: float
    noise_poisson: bool
    ratio: str

    # TODO : Specialize PSF NDArray type
    # Old TODOs
    # - Add PSF & Object shape inputs (instead of only psf)
    # - Add z-phase jitter for the PSF instead of using a fixed plane
    # - Load a simulation parameters file instead of passing everything in the command line
    # - Use input size as alternative
    # - link tqdm with logging
    # - Create a python wrapper for the ImageJ plugin 'DeconvolutionLab2' to generate PSF in the script?
    # - Background noise with different statistics (similar to transient particles)
    def __init__(
        self,
        tracts: Tracts | pathlib.Path = None,
        psf_2d: npt.NDArray | pathlib.Path | None = None,
        resolution: float = 1.0,
        dt: float = 1,
        contrast: float = 5,
        background: float = 0.3,
        noise_gaussian: float = 0.15,
        noise_poisson: bool = True,
        ratio: str = "square",
    ):
        """

        Parameters
        ----------
        tracts
            Tracts or filename with the extension `.csv`, `.json` or `.pcl`.
            A dictionary or a `.csv`, `.json` or `.pcl` filename containing the set of tracts to simulate. The
            dictionary must include the keys `x`, `y`, `t` and `id`.
        psf_2d
            Point-Spread Function (PSF) or a volume filename. If it is a filename, it must be a volume format
            supported by `imageio.volwrite`. Example : `.tif` and `.tiff`.
        resolution
            Spatial resolution [m/px]
        dt
            Temporal resolution  [frame/sec]
        contrast
            Contrast between the simulated particle and the background (Contrast = particle intensity - background
            intensity)
        background
            Background intensity between 0 and 1
        noise_gaussian
            Gaussian noise variance
        noise_poisson
            If True, Poisson noise will be added.
        ratio
            Aspect ratio of the simulated movie. Available ("square"). If none is given, the aspect ratio will be
            inferred from the tracts position.

        """

        # Prepare the simulator
        self.resolution = resolution
        self.dt = dt  # Temporal resolution
        self.contrast = contrast  # Contrast between the simulated particle and the background
        self.background = background  # Background intensity
        self.noise_gaussian = noise_gaussian  # Gaussian noise variance
        self.noise_poisson = noise_poisson  # Poisson noise variance
        self.ratio = ratio
        self.initialized = False

        if isinstance(tracts, Tracts):
            self.tracts = tracts
        elif isinstance(tracts, pathlib.Path):
            self.tracts = load_tracts(tracts)
        elif tracts is None:
            self.tracts = Tracts(x=[], y=[], t=[], id=[])
        else:
            raise TypeError("The passed argument to the `tracts` parameter is of the wrong type.")

        if isinstance(psf_2d, np.ndarray) or psf_2d is None:
            self.psf_2d = psf_2d
        elif isinstance(psf_2d, pathlib.Path):
            self.psf_2d = load_psf(psf_2d)
        else:
            raise TypeError("The passed argument to the `psf_2d` parameter is of the wrong type.")

    def _initialize(self) -> None:
        """Initialize the simulator"""
        assert hasattr(self, "tracts"), "You must load a tracts file or set a tracts dict first"
        self.n_spots = len(self.tracts["x"])

        # Get the number of frames
        self.tmin = 0
        self.tmax = np.max(self.tracts["t"])
        self.n_frames = int((self.tmax - self.tmin) / self.dt) + 1

        # Get the movie shape
        self.xmin = np.min(self.tracts["x"])
        self.ymin = np.min(self.tracts["y"])
        self.xmax = np.max(self.tracts["x"])
        self.ymax = np.max(self.tracts["y"])
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

    def get_estimated_size(self) -> int:
        """Return the estimated movie size in MB"""
        return int(self.nx * self.ny * self.n_frames * 8 / 1000 ** 2)  # Using double precision float (float64)

    def run(self, reinitialize: bool = False) -> None:
        """Run the movie simulation

        Parameters
        ----------
        reinitialize
            If `True`, the simulator will be reinitialized.

        """
        if reinitialize or not self.initialized:
            self._initialize()

        # Create the movie array
        print("Creating an empty movie")
        movie = np.ones((self.n_frames, self.nx, self.ny), dtype=np.float64) * self.background

        # Add Gaussian noise to the background
        if self.noise_gaussian is not None:
            print("Adding gaussian noise to the background")
            movie = skimage.util.random_noise(movie, mode="gaussian", var=self.noise_gaussian)

        # Populate the tracts
        for this_spot in tqdm.tqdm(range(self.n_spots), "Adding tracts"):
            mx = int(np.round((self.tracts["x"][this_spot] - self.xmin) / self.resolution))
            my = int(np.round((self.tracts["y"][this_spot] - self.ymin) / self.resolution))
            mt = int(self.tracts["t"][this_spot] / self.dt)
            if isinstance(mx, list):
                for x, y, t in zip(mx, my, mt):
                    if (0 <= mx < self.nx) and (0 <= my < self.ny):
                        movie[t, x, y] += self.contrast
            else:
                if (0 <= mx < self.nx) and (0 <= my < self.ny):
                    movie[mt, mx, my] += self.contrast

        # TODO : 2D -> 3D
        # Convolve by PSF if provided
        if self.psf_2d is not None:
            px, py = self.psf_2d.shape
            movie = np.pad(movie, ((0, 0), (px // 2, px // 2), (py // 2, py // 2)), mode="reflect")

            # Apply convolution
            for i in tqdm.tqdm(range(self.n_frames), desc="Convolving with PSF"):
                movie[i, ...] = scipy.signal.fftconvolve(movie[i, ...], self.psf_2d, mode="same")

            # Unpad
            # @formatter:off  # TODO : Remove this comment when PyCharm allows a whitespace before ':' in certain cases
            movie = movie[:, px // 2 : px // 2 + self.nx, py // 2 : py // 2 + self.ny]
            # @formatter:on

        # Add Poisson noise
        if self.noise_poisson:
            print("Adding Poisson noise")
            movie = skimage.util.random_noise(movie, mode="poisson", clip=False)
            movie[movie < 0] = 0

        self.movie = movie

    def save(self, filename: pathlib.Path) -> None:
        """Save the simulated movie.
        Parameters
        ----------
        filename
            Output volume filename. Must be a volume format supported by `imageio.volwrite`
        Note
        ----
        The volume will be converted to single precision float (`numpy.float32`)
        """
        assert hasattr(self, "movie"), "You must first run the simulation"

        out_dir = filename.parent
        out_dir.mkdir(parents=True, exist_ok=True)

        imageio.volwrite(filename, self.movie.astype(np.float32))
