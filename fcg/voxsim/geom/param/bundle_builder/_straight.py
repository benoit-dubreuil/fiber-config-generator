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

    centroid_sample_size: int = 1
    begin_position: fcg.typing.Vec3f = (-0.9, 0.0, 0.0)
    end_position: fcg.typing.Vec3f = (1.1, 0.0, 0.0)

    def build(self) -> BundleParams:
        return self._build_bundle([self.begin_position, self.end_position])
