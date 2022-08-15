import dataclasses

from ._bundle import BundleParams


@dataclasses.dataclass()
class StraightBundleParams(BundleParams):
    """The generation parameters of a straight fiber bundle.

    Concrete white fiber configuration generation parameters wrapper of
    :meth:`simulator.factory.geometry_factory.GeometryFactory.create_bundle`.

    Attributes
    ----------

    """

    # TODO
