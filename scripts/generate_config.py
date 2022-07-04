#!/usr/bin/env python

import argparse
import pathlib
import typing

from simulator.factory import GeometryFactory
from simulator.factory.geometry_factory.handlers import GeometryInfos
from simulator.runner import SimulationRunner, SingularityConfig

import fcg.typing

RESOLUTION: typing.Final[fcg.typing.Vec3i] = (10, 10, 10)
SPACING: typing.Final[fcg.typing.Vec3i] = (2, 2, 2)

N_POINT_PER_CENTROID: typing.Final[int] = 5
BUNDLE_RADIUS: typing.Final[float] = 4
BUNDLE_SYMMETRY: typing.Final[float] = 1
BUNDLE_N_FIBERS: typing.Final[int] = 1000
BUNDLE_LIMITS: typing.Final[typing.List[typing.List[float]]] = [[0, 1], [0, 1], [0, 1]]
BUNDLE_CENTER: typing.Final[fcg.typing.Vec3f] = (0.5, 0.5, 0.5)
WORLD_CENTER: typing.Final[fcg.typing.Vec3f] = (5, 5, 5)

DEFAULT_OUT_DIR: typing.Final[pathlib.Path] = pathlib.Path("out")
OUT_GEOM_FILES_PREFIX: typing.Final[str] = "geom"

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
    # Params to fill :
    # run_name = ?
    # phantom_infos = voxsim_geom_params
    # output_folder = out_dir
    # relative_fiber_fraction (optional) -> ???
    # output_nifti (optional) -> ???
    # loop_managed -> default

    # TODO : Supply SingularityConfig to SimulationRunner with custom attribute values
    simulation: SimulationRunner = SimulationRunner()

    simulation.generate_phantom("run_name", voxsim_geom_params, out_dir)


if __name__ == "__main__":
    # TODO : Supply the singularity (*.sif) path as a program arg. See SingularityConfig.
    # TODO : Supply the SingularityCE executable path as a program arg. See SingularityConfig.

    parser = argparse.ArgumentParser("Generate a configuration of white matter fibre bundles")
    parser.add_argument("--out", type=pathlib.Path, help="Output directory for the files")

    args = parser.parse_args()
    dest_dir: pathlib.Path = args.out or pathlib.Path(DEFAULT_OUT_DIR)
    dest_dir.mkdir(parents=True, exist_ok=True)

    print(f"Script execution results are in : {dest_dir}")
    voxsim_geom_params: GeometryInfos = generate_voxsim_geom_params(dest_dir, OUT_GEOM_FILES_PREFIX)
    generate_fiber_tracts(dest_dir, voxsim_geom_params)
