import abc
import dataclasses
import typing

import fcg.typing
from .. import default
from .._bundle import BundleParams


@dataclasses.dataclass
class BundleParamsBuilder(metaclass=abc.ABCMeta):
    """Builder of fiber bundles generation parameters.

    This class builds :class:`fcg.voxsim.geom.param.BundleParams`.

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
    """

    radius: float = default.BUNDLE_RADIUS
    symmetry: float = default.BUNDLE_SYMMETRY
    n_point_per_centroid: int = default.N_POINT_PER_CENTROID

    @abc.abstractmethod
    def build(self, *args, **kwargs) -> BundleParams:
        pass

    @typing.final
    def _build_bundle(self, anchors: list[fcg.typing.Vec3f]) -> BundleParams:
        return BundleParams(radius=radius, symmetry=symmetry, n_point_per_centroid=n_point_per_centroid,
                            anchors=anchors)
