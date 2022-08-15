import dataclasses

import fcg.typing
from . import default as _default

@dataclasses.dataclass()

class WorldParams:
    """White fiber configuration generation parameters wrapper of
    :meth:`simulator.factory.geometry_factory.GeometryFactory.get_geometry_handler`.

    Attributes
    ----------
    resolution
        See the parameter :obj:`resolution` of
        :meth:`simulator.factory.geometry_factory.GeometryFactory.get_geometry_handler`

    """

    resolution: fcg.typing.Vec3i = _default.WORLD_CENTER
