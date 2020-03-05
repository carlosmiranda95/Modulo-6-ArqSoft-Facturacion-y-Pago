from datetime import datetime

from Capa_Modelo_Dominio.Interfaces.IGeneracion import IGeneracion
from Capa_Modelo_Dominio.Entidades.Venta import Venta
from Capa_Modelo_Dominio.Entidades.VentaDetalle import VentaDetalle


class VentaEv(IGeneracion):

    def generar(self, objdata):
        objventa = Venta()
        objventa.Venta_fecha = datetime.utcnow()
        objventa.Venta_montototal = objdata["montototal"]
        listDetalleVenta = []
        for objdetalle in objdata["detalle"]:
            objDetalleVenta = VentaDetalle()
            objDetalleVenta.VentaDetalle_IdVenta = 0
            objDetalleVenta.VentaDetalle_IdProducto = objdetalle["idproducto"]
            objDetalleVenta.VentaDetalle_Cantidad = objdetalle["cantidad"]
            objDetalleVenta.VentaDetalle_subTotal = objdetalle["subtotal"]
            listDetalleVenta.append(objDetalleVenta)
        objrespVenta = {
            "venta": objventa,
            "detalleventa": listDetalleVenta
        }
        return objrespVenta
