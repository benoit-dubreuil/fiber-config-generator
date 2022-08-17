import dataclasses
import typing

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
    centroid_sample_size
        See the parameter :obj:`n_point_per_centroid` of the method
        :meth:`simulator.factory.geometry_factory.GeometryFactory.create_bundle`.
        A greater sample size means a smoother curvature of the centroid spline. It must be greater or equal to ``2``.
        TODO : Test == len(anchors), test < len(anchors), test > len(anchors)
    anchors
        See the parameter :obj:`anchors` of the method
        :meth:`simulator.factory.geometry_factory.GeometryFactory.create_bundle`.
    """

    MIN_CENTROID_SAMPLE_SIZE: typing.Final[typing.ClassVar[int]] = 2

    radius: float = default.BUNDLE_RADIUS
    symmetry: float = default.BUNDLE_SYMMETRY
    centroid_sample_size: int = default.CENTROID_SAMPLE_SIZE
    anchors: list[fcg.typing.Vec3f] = dataclasses.field(default_factory=list)
