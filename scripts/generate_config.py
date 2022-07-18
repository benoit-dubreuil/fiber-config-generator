#!/usr/bin/env python

import argparse
import pathlib

from simulator.factory.geometry_factory.handlers import GeometryInfos
from simulator.runner import SimulationRunner

import fcg.voxsim
from fcg.voxsim.geom.default import OUT_GEOM_FILES_PREFIX
from fcg.voxsim.geom.generator import generate_voxsim_geom_params


def generate_fiber_tracts(out_dir: pathlib.Path, voxsim_geom_params: GeometryInfos) -> None:
    # TODO : Supply SingularityConfig to SimulationRunner with custom attribute values
    simulation: SimulationRunner = SimulationRunner()

    simulation.generate_phantom(fcg.voxsim.default.RUN_NAME, voxsim_geom_params, out_dir, output_nifti=False)


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
    voxsim_geom_params: GeometryInfos = generate_voxsim_geom_params(dest_dir, OUT_GEOM_FILES_PREFIX)
    generate_fiber_tracts(dest_dir, voxsim_geom_params)
