import dataclasses

import fcg.typing

from . import default as _default


@dataclasses.dataclass()
class ClusterParams:
    """White fiber configuration generation parameters wrapper of the method
    :meth:`simulator.factory.geometry_factory.GeometryFactory.create_cluster`.

    Attributes
    ----------
    world_center
        See the parameter :obj:`world_center` of the method
        :meth:`simulator.factory.geometry_factory.GeometryFactory.create_cluster`.
        It is the cluster's position in the world space.

    """

    # TODO : Code getter/setter of this var but renamed as world_position. Make this var private.
    world_center: fcg.typing.Vec3f = _default.CLUSTER_WORLD_POSITION

    # TODO
