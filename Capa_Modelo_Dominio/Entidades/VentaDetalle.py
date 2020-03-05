from sqlalchemy import Column, Integer, Float, ForeignKey
# from Capa_Infraestructura.Persistencia.RepositoryDB import Base
from Capa_Modelo_Dominio.ObjetosValor.BaseModel import Base


class VentaDetalle(Base):
    __tablename__ = "VentaDetalle"

    VentaDetalle_IdVenta = Column(Integer, ForeignKey("Venta.Venta_id"), primary_key=True)
    VentaDetalle_IdProducto = Column(Integer, ForeignKey("Producto.Producto_id"), primary_key=True)
    VentaDetalle_correlativo = Column(Integer, nullable=False, autoincrement=True)
    VentaDetalle_subTotal = Column(Float, nullable=False)
    VentaDetalle_Cantidad = Column(Float, nullable=False)

    def __repr__(self):
        return '<VentaDetalle %r>' % self.VentaDetalle_id
