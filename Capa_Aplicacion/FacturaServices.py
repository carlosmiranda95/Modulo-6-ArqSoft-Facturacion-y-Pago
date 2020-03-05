from flask import Flask, jsonify, Blueprint, request
from Capa_Modelo_Dominio.Eventos.Venta.VentaEv import VentaEv
from Capa_Modelo_Dominio.Entidades.AccesoDb import AccesoDb
from Capa_Infraestructura.Persistencia.FacturaDb import FacturaDb
from Capa_Modelo_Dominio.Eventos.Factura.FacturaEv import FacturaEv
from Capa_Modelo_Dominio.ObjetosValor.JsonResponse import JsonResponse

blueprint = Blueprint('facturas', __name__)


@blueprint.route('/create-invoice/<string:id>', methods=['GET'])
def createinvoice(id):
    content = {"idventa": id}
    objevfactura = FacturaEv()
    objfacturadb = FacturaDb()
    objfactura = objevfactura.generar(content)
    objectventafactura = {"idventa": id, "factura": objfactura}
    if objfacturadb.generar(objectventafactura) == True:
        return JsonResponse.response(0, "Factura Generada Correctamente", {"idfactura": objfacturadb.getComprobante()})
    else:
        return JsonResponse.response(1, "Error al Generar la Factura", {"idfactura": "null"})
