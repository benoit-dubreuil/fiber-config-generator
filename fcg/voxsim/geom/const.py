import typing

import fcg.typing

DIMENSIONALITY: typing.Final[int] = 3
"""See the parameter :obj:`resolution` of :meth:`simulator.factory.geometry_factory.GeometryFactory.create_cluster_meta`
"""

SAMPLING_DISTANCE: typing.Final[float] = 1
"""See the parameter :obj:`sampling_distance` of
:meth:`simulator.factory.geometry_factory.GeometryFactory.create_cluster_meta`
"""

MRI_RESOLUTION: typing.Final[fcg.typing.Vec3i] = (1, 1, 1)
"""See the parameter :obj:`resolution` of
:meth:`simulator.factory.geometry_factory.GeometryFactory.get_geometry_handler`
"""

MRI_VOXEL_SPACING: typing.Final[fcg.typing.Vec3i] = (1, 1, 1)
"""See the parameter :obj:`spacing` of :meth:`simulator.factory.geometry_factory.GeometryFactory.get_geometry_handler`

OUT_GEOM_FILES_PREFIX: typing.Final[str] = "geom"
"""See the parameter :obj:`output_naming` of the method 
:meth:`simulator.factory.geometry_factory.handlers.GeometryHandler.generate_json_configuration_files`.

The Simulation Generator geometry configuration files are prefixed with this string, which itself is suffixed with '_'.
"""
