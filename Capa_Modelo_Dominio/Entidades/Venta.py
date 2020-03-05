import datetime
from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
# from Capa_Infraestructura.Persistencia.RepositoryDB import Base
from Capa_Modelo_Dominio.ObjetosValor.BaseModel import Base


class Venta(Base):
    __tablename__ = 'Venta'

    Venta_id = Column(Integer, primary_key=True, autoincrement=True)
    Venta_fecha = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())
    Venta_montototal = Column(Float, nullable=False)

    def __repr__(self):
        return '<Venta %r>' % self.Venta_id
