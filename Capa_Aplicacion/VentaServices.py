from flask import Flask, jsonify, Blueprint, request
from Capa_Modelo_Dominio.Eventos.Venta.VentaEv import VentaEv
from Capa_Modelo_Dominio.Entidades.AccesoDb import AccesoDb
from Capa_Infraestructura.Persistencia.VentaDb import VentaDb
from Capa_Modelo_Dominio.ObjetosValor.JsonResponse import JsonResponse

blueprint = Blueprint('ventas', __name__)


@blueprint.route('/create-sale', methods=['POST'])
def createsale():
    content = request.json
    objVentaEv = VentaEv()
    objVentaDb = VentaDb()
    if objVentaDb.generar(objVentaEv.generar(content)) == True:
        return JsonResponse.response(0, "Venta realizada Correctamente", {"idventa": objVentaDb.getComprobante()})
    else:
        return JsonResponse.response(1, "Error al realizar la Venta", {"idventa": "null"})
