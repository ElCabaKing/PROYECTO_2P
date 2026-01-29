from flask import Blueprint, request
from src.shared.dependencies import jwt_required_custom
from src.shared.response import response_bad_request
from .controller import HorarioController

horarios_bp = Blueprint('horarios', __name__, url_prefix='/horarios')
controller = HorarioController()


@horarios_bp.route('/', methods=['GET'])
@jwt_required_custom
def listar_horarios():
    sucursal_id = request.args.get('sucursal_id')
    if not sucursal_id:
        return response_bad_request("sucursal_id es requerido")
    return controller.obtener_por_sucursal(sucursal_id)


@horarios_bp.route('/<string:horario_id>', methods=['GET'])
@jwt_required_custom
def obtener_horario(horario_id: str):
    return controller.obtener_por_id(horario_id)


@horarios_bp.route('/', methods=['POST'])
@jwt_required_custom
def crear_horario():
    return controller.crear()


@horarios_bp.route('/<string:horario_id>', methods=['PUT'])
@jwt_required_custom
def actualizar_horario(horario_id: str):
    return controller.actualizar(horario_id)


@horarios_bp.route('/<string:horario_id>', methods=['DELETE'])
@jwt_required_custom
def eliminar_horario(horario_id: str):
    return controller.eliminar(horario_id)
