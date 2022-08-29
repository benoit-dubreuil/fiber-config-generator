#!/usr/bin/env python

import argparse
import pathlib
import typing

import colorama

import fcg.app

_DEFAULT_PSF_PATH: typing.Final[pathlib.Path] = pathlib.Path("psf.tif")
_DEFAULT_FIB_PATH: typing.Final[pathlib.Path] = pathlib.Path("out/phantom/fcg_phantom_merged_bundles.fib")
_DEFAULT_OUT_PATH: typing.Final[pathlib.Path] = pathlib.Path("out.tiff")


class GenerateMicroscopeImg(fcg.app.App):
    """
    TODO

    """

    def _exec_logic(self) -> None:
        parser = argparse.ArgumentParser("Generate a 3D microscope image representation from fiber bundles")
        parser.add_argument(
            "psf",
            type=pathlib.Path,
            default=_DEFAULT_PSF_PATH,
            help='The input path to the PSF. Ex: "./generate_fiber_config.py psf.tif"',
        )
        parser.add_argument(
            "fib",
            type=pathlib.Path,
            default=_DEFAULT_PSF_PATH,
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


if __name__ == "__main__":
    app = GenerateMicroscopeImg()
    app.start()
