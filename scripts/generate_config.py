#!/usr/bin/env python

import argparse
import os
import tempfile
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


def get_geometry_parameters(output_folder, output_naming):
    geometry_handler = GeometryFactory.get_geometry_handler(RESOLUTION, SPACING)

    bundle1 = GeometryFactory.create_bundle(BUNDLE_RADIUS, BUNDLE_SYMMETRY, N_POINT_PER_CENTROID, BASE_ANCHORS)

    cluster = GeometryFactory.create_cluster(
        GeometryFactory.create_cluster_meta(3, BUNDLE_N_FIBERS, 1, BUNDLE_CENTER, BUNDLE_LIMITS),
        [bundle1],
        WORLD_CENTER,
    )

    geometry_handler.add_cluster(cluster)

    return geometry_handler.generate_json_configuration_files(output_naming, output_folder)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Geometry Factory Example Script")
    parser.add_argument("--out", type=str, required=False, help="Output directory for the files")

    args = parser.parse_args()
    if "out" in args and args.out:
        dest = args.out
        os.makedirs(args.out, exist_ok=True)
    else:
        dest = tempfile.mkdtemp(prefix="geo_factory")

    print(f"Script execution results are in : {dest}")
    get_geometry_parameters(dest, "geometry")
