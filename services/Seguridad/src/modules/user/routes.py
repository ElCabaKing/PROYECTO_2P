from flask import Blueprint
from .controller import UserController
from src.middleware.auth import auth_required

user_controller = UserController()

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/new', methods=['POST'])
@auth_required
def new_user():
    return user_controller.new_user()

@user_bp.route('/list', methods=['GET'])
@auth_required
def fetch_user_list():
    return user_controller.fetch_user_list()

@user_bp.route('/<int:user_id>', methods=['PUT'])
@auth_required
def update_user(user_id):
    return user_controller.update_user(user_id)

@user_bp.route('/roles', methods=['GET'])
@auth_required
def fetch_roles():
    return user_controller.fetch_roles()

@user_bp.route('/profile', methods=['GET'])
@auth_required
def get_current_user():
    return user_controller.get_current_user()

@user_bp.route('/view/<int:user_id>', methods=['GET'])
@auth_required
def get_user_by_id(user_id):
    return user_controller.get_user_by_id(user_id)

