import dataclasses

import fcg.typing


@dataclasses.dataclass(frozen=True)
class WorldParams:
    """White fiber configuration generation parameters wrapper of
    :meth:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.get_geometry_handler.
    """

    voxel_resolution: fcg.typing.Vec3i = (1, 1, 1)
    "See :obj:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.get_geometry_handler.resolution"

    # TODO : Necessary? If not, then remove and rename `voxel_resolution` to `resolution`.
    voxel_dimensions: fcg.typing.Vec3i = (1, 1, 1)
    "See :obj:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.get_geometry_handler.spacing"
