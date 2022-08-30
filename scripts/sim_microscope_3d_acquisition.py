#!/usr/bin/env python

import argparse
import pathlib
import typing

import colorama

import fcg.app
from fcg.microscopy import MovieAcquisitionSimulator, load_tracts

_DEFAULT_OUT_PATH: typing.Final[pathlib.Path] = pathlib.Path("out.tiff")


class SimulateMicroscope3dAcquisition(fcg.app.App):
    """
    An application to simulate microscopy movie acquisition (3D) from pregenerated fiber bundles.

    """

    def _exec_logic(self) -> None:
        parser = argparse.ArgumentParser("Simulate microscopy movie acquisition (3D) from fiber bundles")
        parser.add_argument(
            "psf",
            type=pathlib.Path,
            help='Input path to the PSF. Ex: "./sim_microscope_3d_acquisition.py psf.tif"',
        )
        parser.add_argument(
            "fib",
            type=pathlib.Path,
            help="Input path to the generated fiber bundles. The standard file extension is " "'.fib'.",
        )
        parser.add_argument("--out", type=pathlib.Path, default=_DEFAULT_OUT_PATH, help="Output movie file")
        parser.add_argument(
            "-r", "--resolution", default=1, type=float, help="Reconstruction resolution in px (default=%(default)s)"
        )
        parser.add_argument(
            "-tr",
            "--time_resolution",
            default=1,
            type=float,
            help="Reconstruction resolution in frame/seconds (default=%(default)s)",
        )
        parser.add_argument(
            "--contrast",
            default=5,
            type=float,
            help=" Contrast between the simulated particle and the background (Contrast = particle "
            "intensity - background intensity) %(default)s",
        )
        parser.add_argument("--background_intensity", default=0.3, type=float, help="Background intensity %(default)s")
        parser.add_argument(
            "--gaussian_noise_variance",
            default=0.15,
            type=typing.Union[float, None],
            help="Gaussian noise variance (default=%(default)s)",
        )
        parser.add_argument("--poisson_noise", action="store_true", help="Add poisson noise after PSF convolution")

        args = parser.parse_args()

        print("Loading the tracts ... ", end="")
        try:
            fib: pathlib.Path = args.fib
            fib = fib.resolve(strict=True)
            tracts = load_tracts(fib)
            print(colorama.Style.BRIGHT + colorama.Fore.GREEN + "succeeded")
        except Exception as exception:
            print(colorama.Style.BRIGHT + colorama.Fore.RED + "failed")
            raise exception

        simulator = MovieAcquisitionSimulator(
            tracts=tracts,
            resolution=args.resolution,
            dt=args.time_resolution,
            contrast=args.contrast,
            background=args.background_intensity,
            noise_gaussian=args.gaussian_noise_variance,
            noise_poisson=args.poisson_noise,
        )

        print("Loading the PSF ... ", end="")
        try:
            psf: pathlib.Path = args.psf
            psf = psf.resolve(strict=True)

            simulator.load_psf(psf)
            print(colorama.Style.BRIGHT + colorama.Fore.GREEN + "succeeded")
        except Exception as exception:
            print(colorama.Style.BRIGHT + colorama.Fore.RED + "failed")
            raise exception

        print("Simulating the microscopy movie acquisition ... ", end="")
        try:
            simulator.run()
            print(colorama.Style.BRIGHT + colorama.Fore.GREEN + "succeeded")
        except Exception as exception:
            print(colorama.Style.BRIGHT + colorama.Fore.RED + "failed")
            raise exception

        simulator.save(args.out)


if __name__ == "__main__":
    app = SimulateMicroscope3dAcquisition()
    app.start()
