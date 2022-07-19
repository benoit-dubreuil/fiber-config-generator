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
            cls._force_create_singleton()

        return cls.__singleton

    @classmethod
    def _force_create_singleton(cls) -> None:
        singleton_creator = cls._get_singleton_creator()
        cls.__singleton = singleton_creator()

    @classmethod
    def _get_singleton_creator(cls) -> typing.Callable[[], _T]:
        return cls.__init__
