#!/usr/bin/env python

import argparse
import pathlib
import typing

from simulator.factory import GeometryFactory
from simulator.factory.geometry_factory.handlers import GeometryInfos
from simulator.runner import SimulationRunner

import fcg.typing
from fcg.voxsim.default import OUT_DIR, OUT_GEOM_FILES_PREFIX, RUN_NAME

RESOLUTION: typing.Final[fcg.typing.Vec3i] = (10, 10, 10)
SPACING: typing.Final[fcg.typing.Vec3i] = (2, 2, 2)

N_POINT_PER_CENTROID: typing.Final[int] = 5
BUNDLE_RADIUS: typing.Final[float] = 4
BUNDLE_SYMMETRY: typing.Final[float] = 1
BUNDLE_N_FIBERS: typing.Final[int] = 1000
BUNDLE_LIMITS: typing.Final[typing.List[typing.List[float]]] = [[0, 1], [0, 1], [0, 1]]
BUNDLE_CENTER: typing.Final[fcg.typing.Vec3f] = (0.5, 0.5, 0.5)
WORLD_CENTER: typing.Final[fcg.typing.Vec3f] = (5, 5, 5)

BASE_ANCHORS: typing.Final[typing.List[fcg.typing.Vec3f]] = [
    (0.5, -0.3, 0.5),
    (0.5, -0.2, 0.5),
    (0.5, -0.1, 0.5),
    (0.5, 0.0, 0.5),
    (0.5, 0.1, 0.5),
    (0.5, 0.2, 0.5),
    (0.5, 0.3, 0.5),
    (0.5, 0.4, 0.5),
    (0.5, 0.5, 0.5),
    (0.5, 0.6, 0.5),
    (0.5, 0.7, 0.5),
    (0.5, 0.8, 0.5),
    (0.5, 0.9, 0.5),
    (0.5, 1.1, 0.5),
    (0.5, 1.2, 0.5),
    (0.5, 1.3, 0.5),
]


def generate_voxsim_geom_params(out_dir: pathlib.Path, out_files_prefix: str) -> GeometryInfos:
    """
    TODO
    Parameters
    ----------
    out_dir :
    out_files_prefix :

    Returns
    -------

    """
    geometry_handler = GeometryFactory.get_geometry_handler(RESOLUTION, SPACING)

    bundle1 = GeometryFactory.create_bundle(BUNDLE_RADIUS, BUNDLE_SYMMETRY, N_POINT_PER_CENTROID, BASE_ANCHORS)

    cluster = GeometryFactory.create_cluster(
        GeometryFactory.create_cluster_meta(3, BUNDLE_N_FIBERS, 1, BUNDLE_CENTER, BUNDLE_LIMITS),
        [bundle1],
        WORLD_CENTER,
    )

    geometry_handler.add_cluster(cluster)

    return geometry_handler.generate_json_configuration_files(out_files_prefix, out_dir)


def generate_fiber_tracts(out_dir: pathlib.Path, voxsim_geom_params: GeometryInfos) -> None:
    # TODO : Supply SingularityConfig to SimulationRunner with custom attribute values
    simulation: SimulationRunner = SimulationRunner()

    simulation.generate_phantom(RUN_NAME, voxsim_geom_params, out_dir, output_nifti=False)


if __name__ == "__main__":
    # TODO : Supply the singularity (*.sif) path as a program arg. See SingularityConfig.
    # TODO : Supply the SingularityCE executable path as a program arg. See SingularityConfig.

    parser = argparse.ArgumentParser("Generate a configuration of white matter fibre bundles")
    parser.add_argument("--out", type=pathlib.Path, default=OUT_DIR, help="Output directory for the files")

    args = parser.parse_args()
    dest_dir: pathlib.Path = args.out
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_dir = dest_dir.resolve(strict=True)

    print(f"Script execution results are in : {dest_dir}")
    voxsim_geom_params: GeometryInfos = generate_voxsim_geom_params(dest_dir, OUT_GEOM_FILES_PREFIX)
    generate_fiber_tracts(dest_dir, voxsim_geom_params)
