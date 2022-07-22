import logging


class ErrorHandler(logging.Handler):
    _has_emitted_errors: bool
    _has_emitted_critials: bool

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._has_emitted_errors = False
        self._has_emitted_critials = False

    def emit(self, record: logging.LogRecord) -> None:

        if record.levelno == logging.ERROR:
            self._has_emitted_errors = True

        if record.levelno == logging.CRITICAL:
            self._has_emitted_critials = True

    @property
    def has_emitted_errors(self) -> bool:
        return self._has_emitted_errors

    @property
    def has_emitted_criticals(self) -> bool:
        return self._has_emitted_critials
