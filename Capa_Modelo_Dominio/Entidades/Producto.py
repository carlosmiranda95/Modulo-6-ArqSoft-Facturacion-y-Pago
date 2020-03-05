from sqlalchemy import Column, Integer, String, Float
# from Capa_Infraestructura.Persistencia.RepositoryDB import Base
from Capa_Modelo_Dominio.ObjetosValor.BaseModel import Base


class Producto(Base):
    __tablename__ = "Producto"

    Producto_id = Column(Integer, primary_key=True, autoincrement=True)
    Producto_nombre = Column(String(120), nullable=False, unique=True)
    Producto_precio = Column(Float, nullable=False)
    Producto_stock = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Producto %r>' % self.Producto_id
