# TODO : Transform this module into a builder (design pattern).

import pathlib

import simulator.factory as _sim_factory
import simulator.factory.geometry_factory.handlers as _sim_geom_handlers

import fcg.voxsim
import fcg.voxsim.geom as _geom


def generate_voxsim_geom_params(
    root_out_dir: pathlib.Path = fcg.voxsim.default.ROOT_OUT_DIR,
    out_files_prefix: str = _geom.default.OUT_GEOM_FILES_PREFIX,
) -> _sim_geom_handlers.GeometryInfos:
    """
    Generates the VoxSim (through Simulation Generator) geometry parameters configuration files.

    Parameters
    ----------
    out_files_prefix
        The prefix of the generated geometry parameter files.
    root_out_dir
        The directory into which the generated geometry parameter files will be saved. For simplicity, it is usually the
        root output directory of all the other generated files.

    Returns
    -------
    _sim_geom_handlers.GeometryInfos
        The assembled geometry parameters data structure which was used to serialize the geometry parameters.

    """
    geometry_handler: _sim_geom_handlers.GeometryHandler = _sim_factory.GeometryFactory.get_geometry_handler(
        _geom.params.default.RESOLUTION, _geom.const.SPACING
    )

    # TODO : Customise
    bundle1 = _sim_factory.GeometryFactory.create_bundle(
        _geom.params.default.BUNDLE_RADIUS,
        _geom.params.default.BUNDLE_SYMMETRY,
        _geom.params.default.N_POINT_PER_CENTROID,
        _geom.params.default.BASE_ANCHORS,
    )

    cluster = _sim_factory.GeometryFactory.create_cluster(
        _sim_factory.GeometryFactory.create_cluster_meta(
            _geom.const.DIMENSIONALITY,
            _geom.params.default.BUNDLE_N_FIBERS,
            _geom.const.SAMPLING_DISTANCE,
            _geom.params.default.BUNDLE_CENTER,
            _geom.params.default.BUNDLE_LIMITS,
        ),
        [bundle1],
        _geom.params.default.WORLD_CENTER,
    )

    geometry_handler.add_cluster(cluster)

    return geometry_handler.generate_json_configuration_files(out_files_prefix, root_out_dir)
