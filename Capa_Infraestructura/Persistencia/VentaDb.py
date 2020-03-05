from Capa_Modelo_Dominio.Interfaces.IGeneracion import IGeneracion
from Capa_Modelo_Dominio.Entidades.AccesoDb import AccesoDb
from Capa_Infraestructura.Persistencia.RepositoryDB import RepositoryDB
from Capa_Modelo_Dominio.Entidades.Venta import Venta


class VentaDb(IGeneracion):

    def __init__(self):
        self.objaccesodb = AccesoDb()
        self.objrepository = RepositoryDB(self.objaccesodb)
        self.comprobanteVenta = 0

    def generar(self, objdata):
        try:
            objVenta = objdata["venta"]
            self.objrepository.InsertData(objVenta)
            self.objrepository.GetId(objVenta)
            objDetalleVenta = objdata["detalleventa"]
            for detalle in objDetalleVenta:
                detalle.VentaDetalle_IdVenta = objVenta.Venta_id
            self.objrepository.InsertData(objDetalleVenta)
            self.objrepository.CommitDb()
            self.comprobanteVenta = objVenta.Venta_id
            return True
        except(Exception):
            return False

    def getComprobante(self):
        return self.comprobanteVenta
