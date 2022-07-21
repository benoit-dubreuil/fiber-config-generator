import abc


class App(metaclass=abc.ABCMeta):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

# TODO
#   def init(self):
