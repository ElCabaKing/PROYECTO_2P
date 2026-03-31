from flask import Blueprint
from src.shared.dependencies import jwt_required_custom
from .controller import RestauranteController

restaurantes_bp = Blueprint('restaurantes', __name__, url_prefix='/restaurantes')
controller = RestauranteController()


@restaurantes_bp.route('/', methods=['GET'])
@jwt_required_custom
def listar_restaurantes():
    return controller.obtener_todos()


@restaurantes_bp.route('/<restaurante_id>', methods=['GET'])
@jwt_required_custom
def obtener_restaurante(restaurante_id: str):
    return controller.obtener_por_id(restaurante_id)


@restaurantes_bp.route('/', methods=['POST'])
@jwt_required_custom
def crear_restaurante():
    return controller.crear()


@restaurantes_bp.route('/<restaurante_id>', methods=['PUT'])
@jwt_required_custom
def actualizar_restaurante(restaurante_id: str):
    return controller.actualizar(restaurante_id)


@restaurantes_bp.route('/<restaurante_id>', methods=['DELETE'])
@jwt_required_custom
def eliminar_restaurante(restaurante_id: str):
    return controller.eliminar(restaurante_id)
