from flask import Blueprint, request
from src.shared.dependencies import jwt_required_custom
from src.shared.response import response_bad_request
from .controller import PromocionController

promociones_bp = Blueprint('promociones', __name__, url_prefix='/promociones')
controller = PromocionController()


@promociones_bp.route('/', methods=['GET'])
@jwt_required_custom
def listar_promociones():
    sucursal_id = request.args.get('sucursal_id')
    if not sucursal_id:
        return response_bad_request("sucursal_id es requerido")
    return controller.obtener_por_sucursal(sucursal_id)


@promociones_bp.route('/activas', methods=['GET'])
@jwt_required_custom
def listar_promociones_activas():
    sucursal_id = request.args.get('sucursal_id')
    if not sucursal_id:
        return response_bad_request("sucursal_id es requerido")
    return controller.obtener_activas(sucursal_id)


@promociones_bp.route('/<string:promocion_id>', methods=['GET'])
@jwt_required_custom
def obtener_promocion(promocion_id: str):
    return controller.obtener_por_id(promocion_id)


@promociones_bp.route('/', methods=['POST'])
@jwt_required_custom
def crear_promocion():
    return controller.crear()


@promociones_bp.route('/<string:promocion_id>', methods=['PUT'])
@jwt_required_custom
def actualizar_promocion(promocion_id: str):
    return controller.actualizar(promocion_id)


@promociones_bp.route('/<string:promocion_id>', methods=['DELETE'])
@jwt_required_custom
def eliminar_promocion(promocion_id: str):
    return controller.eliminar(promocion_id)
