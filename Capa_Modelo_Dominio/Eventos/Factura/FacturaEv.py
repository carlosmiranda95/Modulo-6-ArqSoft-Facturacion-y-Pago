import uuid
from datetime import datetime

from Capa_Modelo_Dominio.Interfaces.IGeneracion import IGeneracion
from Capa_Modelo_Dominio.Entidades.Factura import Factura


class FacturaEv(IGeneracion):

    def generar(self, objdata):
        objfactura = Factura()
        objfactura.Factura_fk_idventa = objdata["idventa"]
        objfactura.Factura_fecha = datetime.utcnow()
        objfactura.Factura_codigo_control = str(uuid.uuid4())
        return objfactura
