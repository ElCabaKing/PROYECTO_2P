from flask import request, make_response, jsonify
from .services import AuthService
from src.modules.auth.schemas.logInRequest import LogInRequest
from src.modules.auth.schemas.recoveryUserPasswordRequest import RecoveryUserPasswordRequest
from src.modules.auth.schemas.updatePasswordRequest import UpdatePasswordRequest
from .recovery_service import Recovery_Service

class AuthController:
    def __init__(self):
        self.auth_service = AuthService()
        self.recovery_service = Recovery_Service()

    def auth_user(self):
        try:
            schema = LogInRequest()
            log_in_Data = schema.load(request.json)
            access_token = self.auth_service.auth_user(log_in_Data)
            if access_token == None:
                return jsonify({"error": "Credenciales Invalidas"}), 401
            response = make_response({"logIn": True})
            response.set_cookie('access_token', 
                                access_token, 
                                httponly=True, 
                                max_age=60 * 60 * 1000)
            return response, 200
        except ValueError as ve:
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

    def logout(self):
        response = make_response({"logout": True})
        response.set_cookie(
            "access_token","",
            expires=0,
            httponly=True,
        )
        return response, 200

    def recovery_request(self):
        schema = RecoveryUserPasswordRequest()
        user_data = schema.load(request.json)
        self.recovery_service.validate_email(email=user_data['correo'])
            
        return jsonify({"reponse": "Si existe un usuario con ese correo revise su bandeja para cambiar su contrasena"}), 200

    def restore_user_password(self):
        schema = UpdatePasswordRequest()
        request_data = schema.load(request.json)
        self.recovery_service.restore_user_password(
                                                    new_password=request_data['new_password'], 
                                                    confirm_password=request_data['confirm_password'],
                                                    token=request_data['token']
                                                    )
        return jsonify({"validate" : True}), 200