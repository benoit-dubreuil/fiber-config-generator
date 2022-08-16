from ._builder import BundleParamsBuilder
from .._bundle import BundleParams


class StraightBundleParamsBuilder(BundleParamsBuilder):
    """Builder of straight fiber bundles generation parameters.

    This class builds :class:`fcg.voxsim.geom.param.BundleParams` which represent straight fiber bundles. A straight
    fiber bundle forms a straight line. This is why the attribute :attr:`.n_point_per_centroid` is minimized,
    as there is no need to add more details to this simple geometric shape.
    """

    def build(self, radius: float, symmetry: float, n_point_per_centroid: int) -> BundleParams:
        # TODO
        pass
