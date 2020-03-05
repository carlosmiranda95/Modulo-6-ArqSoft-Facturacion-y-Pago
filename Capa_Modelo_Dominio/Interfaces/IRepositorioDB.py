import abc


class IRepositorioDB(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def CommitDb(self):
        raise NotImplementedError

    @abc.abstractmethod
    def InsertData(self, datadb):
        raise NotImplementedError

    @abc.abstractmethod
    def GetAll(self, tabladb):
        raise NotImplementedError

    @abc.abstractmethod
    def GetId(self, entidad):
        raise NotImplementedError
