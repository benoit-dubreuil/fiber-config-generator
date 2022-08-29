import abc
import typing

import colorama


class AppLifeCycleException(RuntimeError):
    """Raised by an instance of the class :class:`fcg.app.App` when calling one of its methods with an inappropriate
    state.

    """


class App(metaclass=abc.ABCMeta):
    """General application for quickly coding executable scripts.

    This class is meant to be inherited by a concrete class in order to define the core program logic by implementing
    the method :meth:`fcg.app.App._exec_logic`. The class :class:`fcg.app.App` wraps the program startup and
    shutdown.

    """

    _is_running: bool = False
    _has_correctly_shutdown: bool = True

    def _pre_start(self, **kwargs) -> None:
        colorama.init(autoreset=True)

    @typing.final
    def start(self, **kwargs) -> None:
        """Starts the application.

        This method also sets up the signal handlers.

        Returns
        -------
        None

        Raises
        ------
        AppLifeCycleException
            If the application is already running.

        """
        if self.is_running:
            raise AppLifeCycleException("Cannot start an app that is already running.")

        self._pre_start(**kwargs)

        self._is_running = True
        self._exec_logic()

        self._shut_down()

    @abc.abstractmethod
    def _exec_logic(self) -> None:
        pass

    def _shutting_down(self, **kwargs) -> None:
        colorama.deinit()

    @typing.final
    def _shut_down(self, **kwargs) -> None:
        """Shuts down the application.

        This method also unsets the signal handlers. It does not actually shut down the application : it performs the
        post-execution cleanup.

        Returns
        -------
        None

        Raises
        ------
        AppLifeCycleException
            If the application is already shutdown.

        """
        if not self.is_running:
            raise AppLifeCycleException("Cannot shut down an app that is already shutdown.")

        self._has_correctly_shutdown = False
        self._is_running = False

        self._shutting_down(**kwargs)

        self._has_correctly_shutdown = True

    @typing.final
    @property
    def is_running(self) -> bool:
        """Gets the status that indicates if the application is running or not.

        In order to be running, the method :meth:`fcg.app.App.start` must have been called and the method
        :meth:`fcg.app.App._shut_down` must not have been called, unless the former was called after the latter.

        Returns
        -------
        bool
            True if the application is running, False otherwise.

        """
        return self._is_running

    @typing.final
    @property
    def has_correctly_shut_down(self) -> bool:
        """Gets the status that indicates if the application has correctly shut down.

        In order to correctly shut down, the application needs to clean everything it has set up, such as signal
        handlers. Also, the method :meth:`fcg.app.App._shut_down` must have been called after the method
        :meth:`fcg.app.App.start` was called.

        Returns
        -------
        bool
            True if the application has correctly shut down, False otherwise.

        """
        return self._has_correctly_shutdown
