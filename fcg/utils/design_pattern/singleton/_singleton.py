import abc
import typing

_T = typing.TypeVar("_T", bound="Singleton")


class Singleton(metaclass=abc.ABCMeta):
    __singleton: typing.ClassVar[typing.Optional[_T]] = None

    def __new__(cls, *args, **kwargs):
        if cls.__singleton is not None:
            raise TypeError("A singleton cannot be instantiated more than once")

        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def get_singleton(cls) -> _T:
        if cls.__singleton is None:
            cls.__singleton = cls()

        return cls.__singleton
