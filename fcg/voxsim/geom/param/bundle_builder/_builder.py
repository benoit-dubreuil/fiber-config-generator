import abc

from .._bundle import BundleParams


class BundleParamsBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def build(self, *args, **kwargs) -> BundleParams:
        pass
