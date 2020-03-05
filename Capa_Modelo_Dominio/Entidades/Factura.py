import datetime
from sqlalchemy import Column, Integer, DateTime, String, Float, ForeignKey
# from Capa_Infraestructura.Persistencia.RepositoryDB import Base
from Capa_Modelo_Dominio.ObjetosValor.BaseModel import Base


class Factura(Base):
    __tablename__ = 'Factura'

    Factura_nrofactura = Column(Integer, primary_key=True, autoincrement=True)
    Factura_fecha = Column(DateTime, default=datetime.datetime.utcnow(), nullable=False)
    Factura_codigo_control = Column(String(120), unique=True, nullable=False)
    Factura_monto_factura = Column(Float, unique=True, nullable=False)
    Factura_fk_idventa = Column(Integer, ForeignKey("Venta.Venta_id"))

    def __repr__(self):
        return '<Factura %r>' % self.Factura_nrofactura
