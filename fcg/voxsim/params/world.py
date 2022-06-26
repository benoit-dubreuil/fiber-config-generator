import dataclasses

import fcg.typing


@dataclasses.dataclass(frozen=True)
class WorldParams:
    """White fiber configuration generation parameters wrappers of
    :meth:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.get_geometry_handler.
    """

    resolution: fcg.typing.Vec3i
    spacing: fcg.typing.Vec3i
