# TODO : Transform this module into a builder (design pattern).

import pathlib

import simulator.factory as _sim_factory
import simulator.factory.geometry_factory.features as _sim_geom_data
import simulator.factory.geometry_factory.handlers as _sim_geom_handlers

import fcg.voxsim

from . import const as _const
from . import param as _param


def _create_voxsim_bundle(bundle_params: _param.BundleParams) -> _sim_geom_data.Bundle:
    return _sim_factory.GeometryFactory.create_bundle(
        radius=bundle_params.radius,
        symmetry=bundle_params.symmetry,
        n_point_per_centroid=bundle_params.centroid_sample_size,
        anchors=bundle_params.anchors,
    )


def _genereate_voxsim_bundle(bundle_params_builder: _param.builder.BundleParamsBuilder) -> _sim_geom_data.Bundle:
    bundle_params = bundle_params_builder.build()
    return _create_voxsim_bundle(bundle_params)


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
    bundle_params_builder = _param.builder.StraightBundleParamsBuilder()
    bundle = _genereate_voxsim_bundle(bundle_params_builder)

    # TODO : Customise
    cluster = _sim_factory.GeometryFactory.create_cluster(
        _sim_factory.GeometryFactory.create_cluster_meta(
            _const.DIMENSIONALITY,
            _param.default.BUNDLE_N_FIBERS,
            _const.SAMPLING_DISTANCE,
            _param.default.BUNDLE_CENTER,
            _param.default.BUNDLE_LIMITS,
        ),
        [bundle],
        _param.default.CLUSTER_WORLD_POSITION,
    )

    geometry_handler.add_cluster(cluster)

    return geometry_handler.generate_json_configuration_files(_const.OUT_GEOM_FILES_PREFIX, root_out_dir)
