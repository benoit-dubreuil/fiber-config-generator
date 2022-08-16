import abc
import typing

import fcg.typing
from .._bundle import BundleParams


class BundleParamsBuilder(metaclass=abc.ABCMeta):
    __radius: float
    __symmetry: float
    __n_point_per_centroid: int

    @abc.abstractmethod
    def build(self, *args, **kwargs) -> BundleParams:
        pass

    @typing.final
    def _build_bundle(self, anchors: list[fcg.typing.Vec3f]) -> BundleParams:
        return BundleParams(radius=radius, symmetry=symmetry, n_point_per_centroid=n_point_per_centroid,
                            anchors=anchors)

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, new_value: float) -> None:
        self.__radius = new_value

    @property
    def symmetry(self) -> float:
        return self.__symmetry

    @symmetry.setter
    def symmetry(self, new_value: float) -> None:
        self.__symmetry = new_value

    @property
    def n_point_per_centroid(self) -> int:
        return self.__n_point_per_centroid

    @n_point_per_centroid.setter
    def n_point_per_centroid(self, new_value: int) -> None:
        self.n_point_per_centroid = new_value
