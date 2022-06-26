#!/usr/bin/env python

import argparse
import os
import tempfile
import typing

from simulator.factory import GeometryFactory

import fcg.typing

resolution: typing.Final[fcg.typing.Vec3i] = (10, 10, 10)
spacing: typing.Final[fcg.typing.Vec3i] = (2, 2, 2)

n_point_per_centroid: typing.Final[int] = 5
bundle_radius: typing.Final[float] = 4
bundle_symmetry: typing.Final[float] = 1
bundle_n_fibers: typing.Final[int] = 1000
bundle_limits: typing.Final[typing.List[typing.List[float]]] = [[0, 1], [0, 1], [0, 1]]
bundle_center: typing.Final[fcg.typing.Vec3f] = (0.5, 0.5, 0.5)
world_center: typing.Final[fcg.typing.Vec3f] = (5, 5, 5)

base_anchors = [
    [0.5, -0.3, 0.5],
    [0.5, -0.2, 0.5],
    [0.5, -0.1, 0.5],
    [0.5, 0, 0.5],
    [0.5, 0.1, 0.5],
    [0.5, 0.2, 0.5],
    [0.5, 0.3, 0.5],
    [0.5, 0.4, 0.5],
    [0.5, 0.5, 0.5],
    [0.5, 0.6, 0.5],
    [0.5, 0.7, 0.5],
    [0.5, 0.8, 0.5],
    [0.5, 0.9, 0.5],
    [0.5, 1.1, 0.5],
    [0.5, 1.2, 0.5],
    [0.5, 1.3, 0.5],
]


def get_geometry_parameters(output_folder, output_naming):
    geometry_handler = GeometryFactory.get_geometry_handler(resolution, spacing)

    bundle1 = GeometryFactory.create_bundle(bundle_radius, bundle_symmetry, n_point_per_centroid, base_anchors)

    cluster = GeometryFactory.create_cluster(
        GeometryFactory.create_cluster_meta(3, bundle_n_fibers, 1, bundle_center, bundle_limits),
        [bundle1],
        world_center,
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
