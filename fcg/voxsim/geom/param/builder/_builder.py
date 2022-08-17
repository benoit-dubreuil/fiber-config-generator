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
        See the attribute :attr:`fcg.voxsim.geom.param.BundleParams.radius`.
    symmetry
        See the attribute ee the attribute :attr:`fcg.voxsim.geom.param.BundleParams.symmetry`.
        See the definition of a cross-section : https://en.wikipedia.org/wiki/Cross_section_(geometry).
    centroid_sample_size
        See the attribute ee the attribute :attr:`fcg.voxsim.geom.param.BundleParams.centroid_sample_size`.
        :meth:`simulator.factory.geometry_factory.GeometryFactory.create_bundle`.
    """

    radius: float = default.BUNDLE_RADIUS
    symmetry: float = default.BUNDLE_SYMMETRY
    centroid_sample_size: int = default.CENTROID_SAMPLE_SIZE

    @abc.abstractmethod
    def build(self) -> BundleParams:
        """Build the :class:`fcg.voxsim.geom.param.BundleParams` from the supplied attributes.

        Returns
        -------
        BundleParams
            A newly created :class:`fcg.voxsim.geom.param.BundleParams`
        """

    @typing.final
    def _build_bundle(self, anchors: list[fcg.typing.Vec3f]) -> BundleParams:
        return BundleParams(
            radius=self.radius, symmetry=self.symmetry, centroid_sample_size=self.centroid_sample_size, anchors=anchors
        )
