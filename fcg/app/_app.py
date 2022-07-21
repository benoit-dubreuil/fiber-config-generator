import abc


class App(metaclass=abc.ABCMeta):
    _is_running: bool = False

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def start(self) -> None:
        # TODO
        ...
        self._is_running = True

    def shutdown(self) -> None:
        self._is_running = False
        # TODO
        ...

    @property
    def is_running(self) -> bool:
        return self._is_running
