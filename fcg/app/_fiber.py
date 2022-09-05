import abc
import signal
import sys
import types
import typing

from ._app import App

_SignalNumber: typing.TypeAlias = int
_SignalHandlerFunc: typing.TypeAlias = typing.Callable[[_SignalNumber, types.FrameType | None], typing.Any]
_SignalHandler: typing.TypeAlias = typing.Union[_SignalHandlerFunc, _SignalNumber, signal.Handlers, None]


class FiberApp(App, metaclass=abc.ABCMeta):
    """Generic Fiber Config Generator application for quickly coding executable scripts.

    In addition to what its parent :class:`fcg.app.App` does, this class handles OS signals as well.

    """

    _preceding_sigterm_handler: _SignalHandler
    _preceding_sigint_handler: _SignalHandler

    def __init__(self) -> None:
        super().__init__()

        self._preceding_sigterm_handler = None
        self._preceding_sigint_handler = None

    def _pre_start(self, **kwargs: typing.Any) -> None:
        assert self._preceding_sigterm_handler is None
        assert self._preceding_sigint_handler is None

        super()._pre_start(**kwargs)

        self._preceding_sigterm_handler = signal.signal(signal.SIGTERM, self._exit_signal_handler())
        self._preceding_sigint_handler = signal.signal(signal.SIGINT, self._exit_signal_handler())

    def _shutting_down(self, **kwargs: typing.Any) -> dict[str, typing.Any]:
        signal.signal(signal.SIGTERM, self._preceding_sigterm_handler)
        self._preceding_sigterm_handler = None

        signal.signal(signal.SIGINT, self._preceding_sigint_handler)
        self._preceding_sigint_handler = None

        return super()._shutting_down(**kwargs)

    def _post_shut_down(self, signum: _SignalNumber | None = None, **kwargs: typing.Any) -> None:
        super()._post_shut_down(**kwargs)

        if signum is not None:
            sys.exit(self._get_signal_exit_code(signum))

    def _exit_signal_handler(self) -> _SignalHandlerFunc:
        def handle_exit_signal(signum: _SignalNumber, _: types.FrameType | None) -> None:
            nonlocal self
            self._shut_down(signum=signum)

        return handle_exit_signal

    @staticmethod
    def _get_signal_exit_code(signum: _SignalNumber) -> int:
        if signum <= 0:
            raise ValueError("A signal number must strictly positive.")

        return 128 + signum
