#!/usr/bin/env python

import argparse
import pathlib

from simulator.factory.geometry_factory.handlers import GeometryInfos

import fcg.voxsim
import fcg.voxsim.geom as _geom
from fcg.voxsim.fiber.generator import generate_fiber_tracts

if __name__ == "__main__":
    # TODO : Supply the singularity (*.sif) path as a program arg. See SingularityConfig.
    # TODO : Supply the SingularityCE executable path as a program arg. See SingularityConfig.

    parser = argparse.ArgumentParser("Generate a configuration of white matter fibre bundles")
    parser.add_argument(
        "--out", type=pathlib.Path, default=fcg.voxsim.default.OUT_DIR, help="Output directory for the files"
    )

    args = parser.parse_args()
    dest_dir: pathlib.Path = args.out
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_dir = dest_dir.resolve(strict=True)

    print(f"Script execution results are in : {dest_dir}")
    voxsim_geom_params: GeometryInfos = _geom.generate_voxsim_geom_params(_geom.default.OUT_GEOM_FILES_PREFIX, dest_dir)
    generate_fiber_tracts(voxsim_geom_params, dest_dir)
