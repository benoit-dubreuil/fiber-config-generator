import dataclasses
import typing


@dataclasses.dataclass(frozen=True)
class World:
    """Configuration wrapper for the initial parameters of
    :py:func:`simulator.factory.geometry_factory.handlers.geometry_handler.GeometryHandler`.

    See :py:func:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.get_geometry_handler`
    """

    resolution: typing.Tuple[int, int, int]
