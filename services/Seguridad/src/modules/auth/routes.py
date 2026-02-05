from flask import Blueprint
from .controller import AuthController


auth_controller = AuthController()




auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/logIn', methods=['POST'])
def new_user():
    return auth_controller.auth_user()

@auth_bp.route('/logOut', methods=['POST'])
def logout():
    return auth_controller.logout()

@auth_bp.route('/recovery_request', methods=['POST'])
def recovery_request():
    return auth_controller.recovery_request()

@auth_bp.route('/recovery', methods=['POST'])
def recovery():
    return auth_controller.restore_user_password()


