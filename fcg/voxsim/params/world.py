import dataclasses

import fcg.typing


@dataclasses.dataclass(frozen=True)
class WorldParams:
    """White fiber configuration generation parameters wrappers of
    :meth:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.get_geometry_handler.
    """

    voxel_resolution: fcg.typing.Vec3i
    "See :obj:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.get_geometry_handler.resolution"

    voxel_dimensions: fcg.typing.Vec3i
    "See :obj:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.get_geometry_handler.spacing"
