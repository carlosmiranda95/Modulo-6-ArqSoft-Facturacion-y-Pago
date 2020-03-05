import abc


class IGeneracion(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def generar(self, objdata):
        raise NotImplementedError
