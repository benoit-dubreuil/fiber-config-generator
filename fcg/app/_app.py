import abc
import typing
import types

_Signal_number = int
_Signal_handler = typing.Union[typing.Callable[[_Signal_number, types.FrameType], None], _Signal_number, None]


class AppLifeCycleException(RuntimeError):
    ...


class App(metaclass=abc.ABCMeta):
    _is_running: bool = False
    _has_correctly_shutdown: bool = True

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def start(self) -> None:
        if self.is_running:
            raise AppLifeCycleException("Cannot start an app that is already running.")

        # TODO
        self._is_running = True

    def shut_down(self) -> None:
        if not self.is_running:
            raise AppLifeCycleException("Cannot shut down an app that is already shutdown.")

        self._has_correctly_shutdown = False
        self._is_running = False

        # TODO

        self._has_correctly_shutdown = True

    @property
    def is_running(self) -> bool:
        return self._is_running

    @property
    def has_correctly_shutdown(self) -> bool:
        return self._has_correctly_shutdown
