from ._builder import BundleParamsBuilder
from .._bundle import BundleParams


class StraightBundleParamsBuilder(BundleParamsBuilder):
    """A builder of generation parameters of straight fiber bundles.

    See :class:`fcg.voxsim.geom.param.bundle.BundleParams`.

    """

    def build(self, radius: float, symmetry: float, n_point_per_centroid: int) -> BundleParams:
        # TODO
        pass
