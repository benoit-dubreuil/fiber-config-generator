import dataclasses

import fcg.typing

from .. import const as _param_const
from .._bundle import BundleParams
from ._builder import BundleParamsBuilder


@dataclasses.dataclass
class ManualBundleParamsBuilder(BundleParamsBuilder):
    """Builder of straight fiber bundles generation parameters.

    This class builds :class:`fcg.voxsim.geom.param.BundleParams` which represent manually defined fiber bundles.

    """

    centroid_sample_size: int = _param_const.MIN_CENTROID_SAMPLE_SIZE * 4
    anchors: list[fcg.typing.Vec3f] = dataclasses.field(default_factory=lambda: [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)])

    def build(self) -> BundleParams:
        return self._build_bundle(anchors)
