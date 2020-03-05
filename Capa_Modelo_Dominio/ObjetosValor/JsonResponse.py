from flask import json, Response

from Capa_Modelo_Dominio.ObjetosValor.AlchemyEncoder import AlchemyEncoder


class JsonResponse:
    @staticmethod
    def response(codigo, mensaje, objectdata):
        data = {'codigo': 0,
                'mensaje': mensaje,
                'data': objectdata}
        return Response(json.dumps(data, cls=AlchemyEncoder), mimetype='application/json')
