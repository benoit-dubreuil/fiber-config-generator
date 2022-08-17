import dataclasses

import fcg.typing
from ._builder import BundleParamsBuilder
from .._bundle import BundleParams


@dataclasses.dataclass
class StraightBundleParamsBuilder(BundleParamsBuilder):
    """Builder of straight fiber bundles generation parameters.

    This class builds :class:`fcg.voxsim.geom.param.BundleParams` which represent straight fiber bundles. A straight
    fiber bundle forms a straight line. This is why the attribute :attr:`.centroid_sample_size` is minimized,
    as there is no need to add more details to this simple geometric shape.
    """

    n_point_per_centroid: int = 1

    def build(self, radius: float, symmetry: float, n_point_per_centroid: int) -> BundleParams:
        anchors: list[fcg.typing.Vec3f] = []
        # TODO
        return self._build_bundle(anchors)
