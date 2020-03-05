from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
from Capa_Modelo_Dominio.Interfaces.IRepositorioDB import IRepositorioDB
from Capa_Modelo_Dominio.ObjetosValor.BaseModel import Base
from collections.abc import Iterable


# Base = declarative_base()

class RepositoryDB(IRepositorioDB):

    def __init__(self, objaccesodb):
        self.engine = create_engine(
            "{0}://{1}@{2}/{3}".format(objaccesodb.conector, objaccesodb.user, objaccesodb.host,
                                       objaccesodb.db),
            convert_unicode=True)
        Base.metadata.reflect(bind=self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.objaccesodb = objaccesodb

    def CommitDb(self):
        self.session.commit()

    def InsertData(self, datadb):
        if isinstance(datadb, Iterable):
            for data in datadb:
                self.session.add(data)
        else:
            self.session.add(datadb)

    def GetAll(self, tabladb):
        return self.session.query(tabladb).all()

    def GetId(self, entidad):
        self.session.flush()
        self.session.refresh(entidad)
