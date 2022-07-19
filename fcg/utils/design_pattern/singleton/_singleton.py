import abc
import typing
import fcg.utils.introspection.caller
import fcg.utils.introspection as _intro

_T = typing.TypeVar("_T", bound="Singleton")


class Singleton(metaclass=abc.ABCMeta):
    __singleton: typing.ClassVar[typing.Optional[_T]] = None

    def __new__(cls, *args, **kwargs):
        if cls.__singleton is not None:
            raise TypeError("A singleton cannot be instantiated more than once")

        caller = _intro.caller.get_caller()

        if hasattr(caller.f_locals, "cls"):
            caller_cls = getattr(caller.f_locals, "cls")

            if hasattr(caller_cls, "get_singleton"):
                ...
        if _intro.caller.get_caller() is not cls.get_singleton:
            raise TypeError("A singleton can only be created implicitly by its special getter")

        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def get_singleton(cls) -> _T:
        if cls.__singleton is None:
            cls.__singleton = cls()

        return cls.__singleton


class Bob(Singleton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


bob = Bob()
print(bob)

bob = Bob.get_singleton()
print(bob)

bob = Bob()
print(bob)
