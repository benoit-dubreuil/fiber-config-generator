#!/usr/bin/env python

import argparse
import pathlib
import typing

import colorama

import fcg.app

_DEFAULT_OUT_PATH: typing.Final[pathlib.Path] = pathlib.Path()


class GenerateMicroscopeImg(fcg.app.App):
    """
    TODO

    """

    def _exec_logic(self) -> None:
        parser = argparse.ArgumentParser("Generate a 3D microscope image representation from fiber bundles")
        parser.add_argument(
            "--out", type=pathlib.Path, default=_DEFAULT_OUT_PATH, help="The output path with the complete filename."
        )

        args = parser.parse_args()

        out: pathlib.Path = args.out
        out_dir = out.parent
        out_dir.mkdir(parents=True, exist_ok=True)
        out = out.resolve(strict=True)


if __name__ == "__main__":
    app = GenerateMicroscopeImg()
    app.start()
