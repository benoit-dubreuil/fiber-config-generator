# TODO : Transform this module into a builder (design pattern).

import pathlib

import simulator.factory as _sim_factory
import simulator.factory.geometry_factory.handlers as _sim_geom_handlers

import fcg.voxsim

from . import const as _const
from . import param as _param


def generate_voxsim_geom_params(
    root_out_dir: pathlib.Path = fcg.voxsim.default.ROOT_OUT_DIR,
) -> _sim_geom_handlers.GeometryInfos:
    """Generates the VoxSim (through Simulation Generator) geometry parameters configuration files.

    Parameters
    ----------
    root_out_dir
        The directory into which the generated geometry parameter files will be saved. For simplicity, it is usually the
        root output directory of all the other generated files.

    Returns
    -------
    _sim_geom_handlers.GeometryInfos
        The assembled geometry parameters data structure which was used to serialize the geometry parameters.

    """
    geometry_handler: _sim_geom_handlers.GeometryHandler = _sim_factory.GeometryFactory.get_geometry_handler(
        _const.MRI_RESOLUTION, _const.MRI_VOXEL_SPACING
    )

    # TODO : Customise
    bundle1 = _sim_factory.GeometryFactory.create_bundle(
        _param.default.BUNDLE_RADIUS,
        _param.default.BUNDLE_SYMMETRY,
        _param.default.N_POINTS_PER_CENTROID,
        _param.default.BASE_ANCHORS,
    )

    cluster = _sim_factory.GeometryFactory.create_cluster(
        _sim_factory.GeometryFactory.create_cluster_meta(
            _const.DIMENSIONALITY,
            _param.default.BUNDLE_N_FIBERS,
            _const.SAMPLING_DISTANCE,
            _param.default.BUNDLE_CENTER,
            _param.default.BUNDLE_LIMITS,
        ),
        [bundle1],
        _param.default.WORLD_CENTER,
    )

    geometry_handler.add_cluster(cluster)

    return geometry_handler.generate_json_configuration_files(_const.OUT_GEOM_FILES_PREFIX, root_out_dir)
