import abc
import signal
import sys
import types
import typing

import colorama

_Signal_number: typing.TypeAlias = int
_Signal_handler: typing.TypeAlias = typing.Union[
    typing.Callable[[_Signal_number, types.FrameType], None], _Signal_number, None]


class AppLifeCycleException(RuntimeError):
    pass


class App(metaclass=abc.ABCMeta):
    _is_running: bool = False
    _has_correctly_shutdown: bool = True
    _preceding_sigterm_handler: _Signal_handler = None
    _preceding_sigint_handler: _Signal_handler = None

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @typing.final
    def start(self) -> None:
        assert self._preceding_sigterm_handler is None
        assert self._preceding_sigint_handler is None

        if self.is_running:
            raise AppLifeCycleException("Cannot start an app that is already running.")

        self._preceding_sigterm_handler = signal.signal(signal.SIGTERM, self._exit_signal_handler())
        self._preceding_sigint_handler = signal.signal(signal.SIGINT, self._exit_signal_handler())

        colorama.init(autoreset=True)

        self._is_running = True
        self._exec_logic()

        self.shut_down()

    @abc.abstractmethod
    def _exec_logic(self) -> None:
        pass

    @typing.final
    def shut_down(self, signum: typing.Optional[_Signal_number] = None) -> None:
        if not self.is_running:
            raise AppLifeCycleException("Cannot shut down an app that is already shutdown.")

        self._has_correctly_shutdown = False
        self._is_running = False

        colorama.deinit()

        signal.signal(signal.SIGTERM, self._preceding_sigterm_handler)
        self._preceding_sigterm_handler = None

        signal.signal(signal.SIGINT, self._preceding_sigint_handler)
        self._preceding_sigint_handler = None

        self._has_correctly_shutdown = True

        if signum is not None:
            sys.exit(self._get_signal_exit_code(signum))

    @typing.final
    @property
    def is_running(self) -> bool:
        return self._is_running

    @typing.final
    @property
    def has_correctly_shutdown(self) -> bool:
        return self._has_correctly_shutdown

    def _exit_signal_handler(self):
        def handle_exit_signal(signum: _Signal_number, frame: types.FrameType) -> None:
            nonlocal self
            self.shut_down(signum=signum)

        return handle_exit_signal

    @staticmethod
    def _get_signal_exit_code(signum: _Signal_number) -> int:
        if signum <= 0:
            raise ValueError("A signal number must strictly positive.")

        return 128 + signum
