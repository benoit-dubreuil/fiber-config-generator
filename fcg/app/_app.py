import abc
import fcg.utils.design_pattern.singleton as _singleton


class App(_singleton.Singleton, metaclass=abc.ABCMeta):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

# TODO
#   def init(self):
