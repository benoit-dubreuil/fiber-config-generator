#!/usr/bin/env python

import argparse
import pathlib
import typing

import colorama

import fcg.app
from fcg.microscopy import Microscope3dAcquisitionSimulator

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
        parser.add_argument(
            "--out", type=pathlib.Path, default=_DEFAULT_OUT_PATH, help="Output movie file"
        )
        parser.add_argument("-r", "--resolution", default=1, type=float,
                            help="Reconstruction resolution in px (default=%(default)s)")
        parser.add_argument("-tr", "--time_resolution", default=1, type=float,
                            help="Reconstruction resolution in frame/seconds (default=%(default)s)")
        parser.add_argument("--square", action="store_true", help="Make the simulated movie square")
        parser.add_argument("--background_intensity", default=0.1, type=float, help="Background intensity %(default)s")
        parser.add_argument("--gaussian_noise", action="store_true", help="Add gaussian noise before PSF convolution")
        parser.add_argument("--gaussian_noise_variance", default=1e-3, type=float,
                            help="Gaussian noise variance (default=%(default)s)")
        parser.add_argument("--poisson_noise", action="store_true", help="Add poisson noise after PSF convolution")

        args = parser.parse_args()

        psf: pathlib.Path = args.psf
        psf = psf.resolve(strict=True)

        fib: pathlib.Path = args.fib
        fib = fib.resolve(strict=True)





        simulator = Microscope3dAcquisitionSimulator()
        simulator.save(args.out)

        # TODO
        print(colorama.Fore.YELLOW + f"TODO : use the psf ({psf}), fib ({fib}) and out ({out})")


if __name__ == "__main__":
    app = SimulateMicroscope3dAcquisition()
    app.start()
