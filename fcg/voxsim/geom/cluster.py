import dataclasses

import fcg.typing


@dataclasses.dataclass(frozen=True)
class ClusterParams:
    """White fiber configuration generation parameters wrapper of
    :meth:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.create_cluster.

    Attributes
    ----------
    world_center : fcg.typing.Vec3i
        See the parameter :python:`world_center` of
        :meth:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.create_cluster
    """

    world_center: fcg.typing.Vec3f = (0.5, 0.5, 0.5)
    "See :obj:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.create_cluster.world_center"

    # TODO
