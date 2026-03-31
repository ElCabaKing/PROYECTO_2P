from flask import Blueprint, request
from src.shared.dependencies import jwt_required_custom
from src.shared.response import response_bad_request
from .controller import MesaController

mesas_bp = Blueprint('mesas', __name__, url_prefix='/mesas')
controller = MesaController()


@mesas_bp.route('/', methods=['GET'])
@jwt_required_custom
def listar_mesas():
    sucursal_id = request.args.get('sucursal_id')
    return controller.obtener_todos(sucursal_id)


@mesas_bp.route('/disponibles', methods=['GET'])
@jwt_required_custom
def obtener_mesas_disponibles():
    sucursal_id = request.args.get('sucursal_id')
    num_personas = request.args.get('num_personas', type=int)

    if not sucursal_id or not num_personas:
        return response_bad_request("sucursal_id y num_personas son requeridos")
    if num_personas < 1:
        return response_bad_request("num_personas debe ser >= 1")

    return controller.obtener_disponibles(sucursal_id, num_personas)


@mesas_bp.route('/<mesa_id>', methods=['GET'])
@jwt_required_custom
def obtener_mesa(mesa_id: str):
    return controller.obtener_por_id(mesa_id)


@mesas_bp.route('/', methods=['POST'])
@jwt_required_custom
def crear_mesa():
    return controller.crear()


@mesas_bp.route('/<mesa_id>', methods=['PUT'])
@jwt_required_custom
def actualizar_mesa(mesa_id: str):
    return controller.actualizar(mesa_id)


@mesas_bp.route('/<mesa_id>', methods=['DELETE'])
@jwt_required_custom
def eliminar_mesa(mesa_id: str):
    return controller.eliminar(mesa_id)
