import dataclasses

import fcg.typing


@dataclasses.dataclass(frozen=True)
class ClusterParams:
    """White fiber configuration generation parameters wrapper of
    :meth:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.create_cluster`.

    Attributes
    ----------
    world_center
        See the parameter :obj:`world_center` of
        :meth:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.create_cluster`
    """

    world_center: fcg.typing.Vec3f = (0.5, 0.5, 0.5)

    # TODO
