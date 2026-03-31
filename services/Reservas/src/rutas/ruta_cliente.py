import common
from flask import request
from ..components.clientes_component import listar_clientes, crear_cliente
from ..utils.database.connection_db import DataBaseHandle
from ..utils.general.logs import HandleLogs
from ..utils.general.response import response_success, response_error


@common.app.route('/api/cliente', methods=['GET', 'POST'])
def _api_clientes():
    try:
        HandleLogs.write_log("Servicio reserva")
        match request.method:
            case 'GET':  return _listar_clientes()
            case 'POST': return _crear_cliente(
                request.json['nombre'],
                request.json['contrasenya'],
            )
            case _: return response_error("Peticion incorrecta")
    except Exception as err:
        HandleLogs.write_error(err)
        return response_error(err.__str__())

def _listar_clientes():
    res = listar_clientes()
    if res['result']:
        return response_success(res['data'])
    else:
        return response_error(res['message'])

def _crear_cliente(nombre, contacto):
    res = crear_cliente(nombre, contacto)
    if res['result']:
        return response_success(res['data'])
    else:
        return response_error(res['message'])
