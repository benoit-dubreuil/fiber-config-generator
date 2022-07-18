import pathlib

from fcg.voxsim.cli.default import OUT_DIR
from fcg.voxsim.geom.default import OUT_GEOM_FILES_PREFIX
from fcg.voxsim.geom.params.default import (
    RESOLUTION,
    SPACING,
    N_POINT_PER_CENTROID,
    BUNDLE_RADIUS,
    BUNDLE_SYMMETRY,
    BUNDLE_N_FIBERS,
    BUNDLE_LIMITS,
    BUNDLE_CENTER,
    WORLD_CENTER,
    BASE_ANCHORS,
)
from simulator.factory import GeometryFactory
from simulator.factory.geometry_factory.handlers import GeometryInfos


def generate_voxsim_geom_params(
    out_dir: pathlib.Path = OUT_DIR, out_files_prefix: str = OUT_GEOM_FILES_PREFIX
) -> GeometryInfos:
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
