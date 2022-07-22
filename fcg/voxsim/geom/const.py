import typing

import fcg.typing

DIMENSIONALITY: typing.Final[int] = 3
"""See the parameter :obj:`resolution` of :meth:`simulator.factory.geometry_factory.GeometryFactory.create_cluster_meta`
"""

SAMPLING_DISTANCE: typing.Final[float] = 1
"""See the parameter :obj:`sampling_distance` of 
:meth:`simulator.factory.geometry_factory.GeometryFactory.create_cluster_meta`
"""

SPACING: typing.Final[fcg.typing.Vec3i] = (1, 1, 1)
"""See the parameter :obj:`spacing` of :meth:`simulator.factory.geometry_factory.GeometryFactory.get_geometry_handler`
"""
