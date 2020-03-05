from Capa_Modelo_Dominio.Interfaces.IGeneracion import IGeneracion
from Capa_Modelo_Dominio.Entidades.AccesoDb import AccesoDb
from Capa_Infraestructura.Persistencia.RepositoryDB import RepositoryDB
from Capa_Modelo_Dominio.Entidades.Venta import Venta


class FacturaDb(IGeneracion):

    def __init__(self):
        self.objaccesodb = AccesoDb()
        self.objrepository = RepositoryDB(self.objaccesodb)
        self.comprobantefactura = 0

    def generar(self, objdata):
        idventa = int(objdata["idventa"])
        objfactura = objdata["factura"]
        pivot = False
        dataVenta = self.objrepository.GetAll(Venta)
        for data in dataVenta:
            if data.Venta_id == idventa:
                objfactura.Factura_fk_idventa = idventa
                objfactura.Factura_monto_factura = data.Venta_montototal
                pivot = True
                break

        if pivot == True:
            self.objrepository.InsertData(objfactura)
            self.objrepository.CommitDb()
            self.comprobantefactura = objfactura.Factura_monto_factura
            return True
        else:
            return False

    def generarComprobante(self):
        return self.comprobantefactura
