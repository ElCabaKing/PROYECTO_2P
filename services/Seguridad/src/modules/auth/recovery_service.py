from .model import AuthModel
from src.utils.Url_Generator import generar_token, validate_recovery_token
from src.utils.Email_Sender import send_email
from flask import current_app
from core.exceptions import AppError
from bcrypt import hashpw, gensalt
import threading

class Recovery_Service:
    
    def __init__(self):
        self.auth_model = AuthModel()
        
    def recovery_user_password(self, email,id):
        brute_token = generar_token(id)
        app = current_app._get_current_object()
        threading.Thread(
        target=send_email,
        args=(app, email,f"""Acceda al siguiente enlace para recuperar su contrasen:
              http://localhost:3000/reset-password/{brute_token}""","Recuperacion de Contrasena"),
        daemon=True
        ).start()
        return 
    
    def validate_email(self, email):
        user = self.auth_model.get_user_by_email(email)
        if user is None:
            return 
        return self.recovery_user_password(email, user['id'])
    
    def validate_token(self, token):
        user_id = validate_recovery_token(token)
        user_data = self.auth_model.get_user_by_id(user_id)
        print(user_data)
        return user_data
    
    def restore_user_password(self, new_password,confirm_password,token):
        user_data =self.validate_token(token)
        if new_password != confirm_password:
            raise AppError("Las contraseñas no coinciden")
        password_hash = hashpw(new_password.encode('utf-8'), gensalt())
        
        self.auth_model.update_user_password(user_data['id'], password_hash.decode('utf-8'))
        app = current_app._get_current_object()
        threading.Thread(
        target=send_email,
        args=(app, user_data['correo'],f"""Se cambio su contrasena exitosamente""","Recuperacion de Contrasena"),
        daemon=True
        ).start()
        return None
        

