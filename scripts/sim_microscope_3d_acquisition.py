#!/usr/bin/env python

import argparse
import pathlib
import typing

import colorama

import fcg.app

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
            help='The input path to the PSF. Ex: "./sim_microscope_3d_acquisition.py psf.tif"',
        )
        parser.add_argument(
            "fib",
            type=pathlib.Path,
            help="The input path to the generated fiber bundles. The standard file extension is " "'.fib'.",
        )
        parser.add_argument(
            "--out", type=pathlib.Path, default=_DEFAULT_OUT_PATH, help="The output path with the complete filename."
        )

        args = parser.parse_args()

        psf: pathlib.Path = args.psf
        psf = psf.resolve(strict=True)

        fib: pathlib.Path = args.fib
        fib = fib.resolve(strict=True)

        out: pathlib.Path = args.out
        out_dir = out.parent
        out_dir.mkdir(parents=True, exist_ok=True)
        out_dir = out_dir.resolve(strict=True)

        # TODO
        print(colorama.Fore.YELLOW + f"TODO : use the psf ({psf}), fib ({fib}) and out_dir ({out_dir})")


if __name__ == "__main__":
    app = SimulateMicroscope3dAcquisition()
    app.start()
