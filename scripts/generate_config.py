#!/usr/bin/env python

import argparse
import pathlib
import typing

from simulator.factory import GeometryFactory

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


def generate_voxsim_geom_params(out_dir, out_files_prefix):
    geometry_handler = GeometryFactory.get_geometry_handler(RESOLUTION, SPACING)

    bundle1 = GeometryFactory.create_bundle(BUNDLE_RADIUS, BUNDLE_SYMMETRY, N_POINT_PER_CENTROID, BASE_ANCHORS)

    cluster = GeometryFactory.create_cluster(
        GeometryFactory.create_cluster_meta(3, BUNDLE_N_FIBERS, 1, BUNDLE_CENTER, BUNDLE_LIMITS),
        [bundle1],
        WORLD_CENTER,
    )

    geometry_handler.add_cluster(cluster)

    return geometry_handler.generate_json_configuration_files(out_files_prefix, out_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Generate a configuration of white matter fibre bundles")
    parser.add_argument("--out", type=pathlib.Path, required=False, help="Output directory for the files")

    args = parser.parse_args()
    out_dir: pathlib.Path = args.out or pathlib.Path(DEFAULT_OUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Script execution results are in : {out_dir}")
    generate_voxsim_geom_params(out_dir, OUT_GEOM_FILES_PREFIX)
