from flask_jwt_extended import create_access_token
from .model import AuthModel
from src.modules.auth.schemas.userPayload import UserPayload
from core.exceptions import UnauthorizedError
from bcrypt import checkpw, gensalt, hashpw


class AuthService:
    def __init__(self):
        self.auth_model = AuthModel()

    def auth_user(this, log_in_Data):
        user_data = this.auth_model.get_user_by_cid(log_in_Data)
        if user_data is None:
            return None
        if checkpw(log_in_Data['Contrasena'].encode('utf-8'), 
                user_data['contrasenahash'].encode('utf-8')):
            access_token = create_access_token(identity=user_data['cedula'],
                                            additional_claims={"role": user_data['roleid'],
                                                               "sucursal_id": user_data['sucursalid'],
                                                               "user_id": user_data['id'],
                                                               "restauran_id": user_data['restauranid']})
            return access_token

