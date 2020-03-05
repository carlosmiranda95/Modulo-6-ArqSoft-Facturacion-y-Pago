from flask import Blueprint, Response
from Capa_Infraestructura.Persistencia.RepositoryDB import RepositoryDB
from Capa_Modelo_Dominio.Entidades.AccesoDb import AccesoDb
from Capa_Modelo_Dominio.Entidades.Producto import Producto
import json

from Capa_Modelo_Dominio.ObjetosValor.AlchemyEncoder import AlchemyEncoder
from Capa_Modelo_Dominio.ObjetosValor.JsonResponse import JsonResponse

blueprint = Blueprint('productos', __name__)

objAccesoDb = AccesoDb()


@blueprint.route('/getproduct', methods=['GET'])
def getproduct():
    objrepository = RepositoryDB(objAccesoDb)
    dataquery = objrepository.GetAll(Producto)
    return JsonResponse.response(0, 'Consulta Exitosa', dataquery)
