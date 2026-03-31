from flask import Blueprint, request
from src.shared.dependencies import jwt_required_custom
from .controller import SucursalController

sucursales_bp = Blueprint('sucursales', __name__, url_prefix='/sucursales')
controller = SucursalController()


@sucursales_bp.route('/', methods=['GET'])
@jwt_required_custom
def listar_sucursales():
    """Get all branches, optionally filtered by restaurant_id query param."""
    restaurante_id = request.args.get('restaurante_id')
    return controller.obtener_todos(restaurante_id)


@sucursales_bp.route('/<sucursal_id>', methods=['GET'])
@jwt_required_custom
def obtener_sucursal(sucursal_id: str):
    """Get a branch by ID."""
    return controller.obtener_por_id(sucursal_id)


@sucursales_bp.route('/', methods=['POST'])
@jwt_required_custom
def crear_sucursal():
    """Create a new branch."""
    return controller.crear()


@sucursales_bp.route('/<sucursal_id>', methods=['PUT'])
@jwt_required_custom
def actualizar_sucursal(sucursal_id: str):
    """Update a branch."""
    return controller.actualizar(sucursal_id)


@sucursales_bp.route('/<sucursal_id>', methods=['DELETE'])
@jwt_required_custom
def eliminar_sucursal(sucursal_id: str):
    """Delete a branch."""
    return controller.eliminar(sucursal_id)
