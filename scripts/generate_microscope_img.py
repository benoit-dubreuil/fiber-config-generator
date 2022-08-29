#!/usr/bin/env python

import argparse
import pathlib
import typing

import colorama
from simulator.factory.geometry_factory.handlers import GeometryInfos

import fcg.app
import fcg.voxsim
import fcg.voxsim.geom as _geom
import fcg.voxsim.phantom as _phantom

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
        out_dir: pathlib.Path = args.out
        out_dir.mkdir(parents=True, exist_ok=True)
        out_dir = out_dir.resolve(strict=True)

        print(f"Script execution results directory : {out_dir}")

        print("Generating voXSim geometry parameters ... ", end="")
        try:
            voxsim_geom_params: GeometryInfos = _geom.generate_voxsim_geom_params(out_dir)
            print(colorama.Style.BRIGHT + colorama.Fore.GREEN + "succeeded")
        except Exception as exception:
            print(colorama.Style.BRIGHT + colorama.Fore.RED + "failed")
            raise exception

        print("Generating the white matter phantom ... ", end="")
        try:
            returncode: int = _phantom.generate_phantom(voxsim_geom_params, out_dir)

            if returncode:
                print(colorama.Style.BRIGHT + colorama.Fore.RED + "failed")
            else:
                print(colorama.Style.BRIGHT + colorama.Fore.GREEN + "succeeded")
        except Exception as exception:
            print(colorama.Style.BRIGHT + colorama.Fore.RED + "failed")
            raise exception


if __name__ == "__main__":
    app = GenerateMicroscopeImg()
    app.start()
