"""Standardized response functions for the API."""


def response_inserted(datos):
    """Response for successful INSERT operations (201)."""
    return {
        'result': True,
        'message': "Registro insertado con éxito",
        'data': datos,
        'status_code': 201,
    }, 201


def response_updated(datos):
    """Response for successful UPDATE operations (200)."""
    return {
        'result': True,
        'message': "Registro actualizado con éxito",
        'data': datos,
        'status_code': 200,
    }, 200


def response_deleted():
    """Response for successful DELETE operations (200)."""
    return {
        'result': True,
        'message': "Registro eliminado con éxito",
        'data': {},
        'status_code': 200,
    }, 200


def response_not_found(mensaje="No hay datos para la consulta"):
    """Response when no data is found (404)."""
    return {
        'result': False,
        'message': mensaje,
        'data': {},
        'status_code': 404,
    }, 404


def response_success(datos):
    """Response for successful GET operations (200)."""
    return {
        'result': True,
        'message': "Exitoso",
        'data': datos,
        'status_code': 200,
    }, 200


def response_error(mensaje):
    """Response for server errors (500)."""
    return {
        'result': False,
        'message': mensaje,
        'data': {},
        'status_code': 500,
    }, 500


def response_bad_request(mensaje):
    """Response for validation errors (400)."""
    return {
        'result': False,
        'message': mensaje,
        'data': {},
        'status_code': 400,
    }, 400


def response_unauthorize():
    """Response for unauthorized access (401)."""
    return {
        'result': False,
        'message': "Acceso no autorizado",
        'data': {},
        'status_code': 401,
    }, 401


def response_forbidden(mensaje="No tiene permisos para realizar esta acción"):
    """Response for forbidden access (403)."""
    return {
        'result': False,
        'message': mensaje,
        'data': {},
        'status_code': 403,
    }, 403


def internal_response(result, datos, mensaje):
    """Internal response for method returns (not HTTP)."""
    return {
        'result': result,
        'data': datos,
        'message': mensaje
    }
