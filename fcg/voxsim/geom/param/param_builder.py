import abc


class GeomParamBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def bob(self, *args, **kwargs):
        pass
