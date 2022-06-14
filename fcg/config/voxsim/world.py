import dataclasses
import fcg.typing


@dataclasses.dataclass(frozen=True)
class World:
    """Configuration wrapper for the initial parameters of
    :py:func:`simulator.factory.geometry_factory.handlers.geometry_handler.GeometryHandler`.

    See :py:meth:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.get_geometry_handler`
    """

    resolution: fcg.typing.Vec3i
    spacing: fcg.typing.Vec3i
