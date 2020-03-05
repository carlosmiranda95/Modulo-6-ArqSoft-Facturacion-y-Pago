from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Capa_Infraestructura.Persistencia.RepositoryDB import RepositoryDB
from Capa_Infraestructura.Persistencia.RepositoryDB import Base
from Capa_Modelo_Dominio.Entidades.AccesoDb import AccesoDb
from Capa_Modelo_Dominio.Entidades.Producto import Producto

objAccesoDb = AccesoDb()

engine = create_engine(
    "{0}://{1}@{2}".format(objAccesoDb.conector, objAccesoDb.user, objAccesoDb.host),
    convert_unicode=True)
engine.execute("CREATE DATABASE {0}".format(objAccesoDb.db))
engine = create_engine(
    "{0}://{1}@{2}/{3}".format(objAccesoDb.conector, objAccesoDb.user, objAccesoDb.host,
                               objAccesoDb.db),
    convert_unicode=True)
Base.metadata.reflect(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
import Capa_Modelo_Dominio.Entidades.Producto
import Capa_Modelo_Dominio.Entidades.Venta
import Capa_Modelo_Dominio.Entidades.VentaDetalle
import Capa_Modelo_Dominio.Entidades.Factura
Base.metadata.create_all(engine)
objRepositorioDb = RepositoryDB(objAccesoDb)
objListData = []
objProducto1 = Producto(Producto_nombre="Barra_de_Proteinas", Producto_precio=10.5, Producto_stock=11)
objProducto2 = Producto(Producto_nombre="Batido de Proteinas", Producto_precio=105.5, Producto_stock=12)
objProducto3 = Producto(Producto_nombre="Cereal Integral", Producto_precio=15.8, Producto_stock=13)
objProducto4 = Producto(Producto_nombre="Omega 3", Producto_precio=56.4, Producto_stock=14)
objProducto5 = Producto(Producto_nombre="Leche de Soya", Producto_precio=6.5, Producto_stock=15)
objProducto6 = Producto(Producto_nombre="Pasta Dental Colgate Total 12", Producto_precio=12, Producto_stock=16)
objListData.append(objProducto1)
objListData.append(objProducto2)
objListData.append(objProducto3)
objListData.append(objProducto4)
objListData.append(objProducto5)
objListData.append(objProducto6)
objRepositorioDb.InsertData(objListData)
objRepositorioDb.CommitDb()
