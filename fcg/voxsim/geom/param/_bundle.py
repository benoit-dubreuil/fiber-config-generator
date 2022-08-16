import dataclasses

import fcg.typing
from . import default


@dataclasses.dataclass()
class BundleParams:
    """The generation parameters of a fiber bundle.

    This class is a white fiber configuration generation parameters wrapper of
    :meth:`simulator.factory.geometry_factory.GeometryFactory.create_bundle`.

    Attributes
    ----------
    radius
        See the parameter :obj:`radius` of the method
        :meth:`simulator.factory.geometry_factory.GeometryFactory.create_bundle`.
    symmetry
        See the parameter :obj:`symmetry` of the method
        :meth:`simulator.factory.geometry_factory.GeometryFactory.create_bundle`.
        See the definition of a cross-section : https://en.wikipedia.org/wiki/Cross_section_(geometry).
    n_point_per_centroid
        See the parameter :obj:`n_point_per_centroid` of the method
        :meth:`simulator.factory.geometry_factory.GeometryFactory.create_bundle`.
    anchors
        See the parameter :obj:`anchors` of the method
        :meth:`simulator.factory.geometry_factory.GeometryFactory.create_bundle`.
    """

    radius: float = default.BUNDLE_RADIUS
    symmetry: float = default.BUNDLE_SYMMETRY
    n_point_per_centroid: int = default.N_POINT_PER_CENTROID
    anchors: list[fcg.typing.Vec3f] = dataclasses.field(default_factory=list)
