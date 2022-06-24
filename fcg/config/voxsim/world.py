import dataclasses

import fcg.typing


@dataclasses.dataclass(frozen=True)
class World:
    """Configuration wrapper for the initial parameters of
    :func:`simulator.factory.geometry_factory.handlers.geometry_handler.GeometryHandler`.

    See :meth:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.get_geometry_handler`

    Attributes
    ----------
    resolution : :obj:`fcg.typing.Vec3i`
        See :meth:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.get_geometry_handler`
    spacing : :obj:`fcg.typing.Vec3i`
        See :meth:`simulator.factory.geometry_factory.geometry_factory.GeometryFactory.get_geometry_handler`

    """

    resolution: fcg.typing.Vec3i
    spacing: fcg.typing.Vec3i
