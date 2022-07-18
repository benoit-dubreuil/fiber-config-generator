import pathlib

import simulator.factory as _sim_factory
import simulator.factory.geometry_factory.handlers as _sim_geom_handlers

import fcg.voxsim.cli as _cli
import fcg.voxsim.geom as _geom


def generate_voxsim_geom_params(
    out_dir: pathlib.Path = _cli.default.OUT_DIR, out_files_prefix: str = _geom.default.OUT_GEOM_FILES_PREFIX
) -> _sim_geom_handlers.GeometryInfos:
    """
    TODO
    Parameters
    ----------
    out_dir :
    out_files_prefix :

    Returns
    -------

    """
    geometry_handler = _sim_factory.GeometryFactory.get_geometry_handler(
        _geom.params.default.RESOLUTION, _geom.params.default.SPACING
    )

    bundle1 = _sim_factory.GeometryFactory.create_bundle(
        _geom.params.default.BUNDLE_RADIUS,
        _geom.params.default.BUNDLE_SYMMETRY,
        _geom.params.default.N_POINT_PER_CENTROID,
        _geom.params.default.BASE_ANCHORS,
    )

    cluster = _sim_factory.GeometryFactory.create_cluster(
        _sim_factory.GeometryFactory.create_cluster_meta(
            3,
            _geom.params.default.BUNDLE_N_FIBERS,
            1,
            _geom.params.default.BUNDLE_CENTER,
            _geom.params.default.BUNDLE_LIMITS,
        ),
        [bundle1],
        _geom.params.default.WORLD_CENTER,
    )

    geometry_handler.add_cluster(cluster)

    return geometry_handler.generate_json_configuration_files(out_files_prefix, out_dir)
