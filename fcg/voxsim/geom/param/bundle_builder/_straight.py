from ._builder import BundleParamsBuilder
from .._bundle import BundleParams


class StraightBundleParamsBuilder(BundleParamsBuilder):
    """Builder of straight fiber bundles generation parameters.

    This class builds :class:`fcg.voxsim.geom.param.BundleParams` which represent straight fiber bundles. A straight
    fiber bundle forms a straight line.
    """

    def build(self, radius: float, symmetry: float, n_point_per_centroid: int) -> BundleParams:
        # TODO
        pass
