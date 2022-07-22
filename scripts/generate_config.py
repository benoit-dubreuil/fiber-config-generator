#!/usr/bin/env python

import argparse
import pathlib

import colorama
from simulator.factory.geometry_factory.handlers import GeometryInfos

import fcg.app
import fcg.voxsim
import fcg.voxsim.geom as _geom
import fcg.voxsim.phantom as _fiber
import fcg.voxsim.phantom.generator


class GenerateStraigthBundle(fcg.app.App):
    def _exec_logic(self) -> None:
        # TODO : Supply the singularity (*.sif) path as a program arg. See SingularityConfig.
        # TODO : Supply the SingularityCE executable path as a program arg. See SingularityConfig.

        parser = argparse.ArgumentParser("Generate a configuration of white matter fibre bundles")
        parser.add_argument(
            "--out", type=pathlib.Path, default=fcg.voxsim.default.ROOT_OUT_DIR, help="Output directory for the files"
        )

        args = parser.parse_args()
        out_dir: pathlib.Path = args.out
        out_dir.mkdir(parents=True, exist_ok=True)
        out_dir = out_dir.resolve(strict=True)

        print(f"Script execution results directory : {out_dir}")

        print("Generating VoxSim geometry parameters ... ", end="")
        try:
            voxsim_geom_params: GeometryInfos = _geom.generate_voxsim_geom_params(out_dir)
            print(colorama.Fore.GREEN + "succeeded")
        except Exception as e:
            print(colorama.Fore.RED + "failed")
            raise e

        print("Generating the white matter phantom ... ", end="")
        try:
            _fiber.generator.generate_fiber_tracts(voxsim_geom_params, out_dir)
            print(colorama.Fore.GREEN + "succeeded")
        except Exception as e:
            print(colorama.Fore.RED + "failed")
            raise e


if __name__ == "__main__":
    app = GenerateStraigthBundle()
    app.start()
