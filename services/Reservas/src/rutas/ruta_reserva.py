import common
from flask import request
from ..components.reservas_component import listar_reservas, \
                                            crear_reserva, \
                                            cancelar_reserva, \
                                            checkin_reserva
from ..utils.database.connection_db import DataBaseHandle
from ..utils.general.logs import HandleLogs
from ..utils.general.response import response_success, response_error


@common.app.route('/api/reserva', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def _api_reserva():
    try:
        HandleLogs.write_log("Servicio reserva")
        match request.method:
            case 'GET': return _listar_reservas()
            case 'POST': return _crear_reserva(
                request.json['cliente'],
                request.json['restaurante'],
                request.json['fini'],
                request.json['ffin'],
            )
            case 'DELETE': return _cancelar_reserva(request.json['id'])
            case 'PATCH': return _checkin_reserva(request.json['id'])
            case _: return response_error("Peticion incorrecta")
    except Exception as err:
        HandleLogs.write_error(err)
        return response_error(err.__str__())

def _listar_reservas():
    res = listar_reservas()
    if res['result']:
        return response_success(res['data'])
    else:
        return response_error(res['message'])

def _crear_reserva(cliente, restaurante, fini, ffin):
    res = crear_reserva(cliente, restaurante, fini, ffin)
    if res['result']:
        return response_success(res['data'])
    else:
        return response_error(res['message'])

def _cancelar_reserva(reserva):
    res = cancelar_reserva(reserva)
    if res['result']:
        return response_success(res['data'])
    else:
        return response_error(res['message'])

def _checkin_reserva(reserva):
    res = checkin_reserva(reserva)
    if res['result']:
        return response_success(res['data'])
    else:
        return response_error(res['message'])
