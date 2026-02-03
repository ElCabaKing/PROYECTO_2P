from flask_jwt_extended import create_access_token
from .model import AuthModel
from core.exceptions import UnauthorizedError
from bcrypt import checkpw


class AuthService:
    def __init__(self):
        self.auth_model = AuthModel()

    def auth_user(this, log_in_Data):
        user_data = this.auth_model.get_user_by_cid(log_in_Data)
        if user_data is None:
            raise UnauthorizedError("Credenciales Invalidas")
        if not checkpw(log_in_Data['contrasena'].encode('utf-8'), 
                user_data['contrasena_hash'].encode('utf-8')):
            raise UnauthorizedError("Credenciales Invalidas")
        access_token = create_access_token(identity=user_data['cedula'],
                                        additional_claims={"role": user_data['role_id'],
                                                           "sucursal_id": user_data['sucursal_id'],
                                                           "user_id": user_data['id'],
                                                           "restaurant_id": user_data['restaurant_id']})
        return access_token

