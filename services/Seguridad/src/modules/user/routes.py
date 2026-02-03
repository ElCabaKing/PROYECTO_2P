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
