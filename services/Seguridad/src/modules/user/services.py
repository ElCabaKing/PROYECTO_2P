from .model import UserModel
from bcrypt import hashpw, gensalt
from src.utils.Email_Sender import send_email
from flask import current_app
import threading


class UserService:
    
    def __init__(self):
        self.user_model = UserModel()

    def create_user(self, user):    
        password_hash = hashpw(user['Contrasena'].encode(), gensalt())
        user['Contrasena'] = password_hash
        response = self.user_model.insert_new_user(user)
        app = current_app._get_current_object()
        threading.Thread(
        target=send_email,
        args=(app, user['Correo'],"Bienvenido","Bienvenido a nuestro equipo"),
        daemon=True
        ).start()
        return response

    def fetch_user_list(self, index_num, sucursal_id):
        num_offset = (index_num['indexNum'] - 1) * 10
        return self.user_model.get_user_list(num_offset, sucursal_id)
    
    def fetch_user_list(self, index_num, restaurant_id):
        num_offset = (index_num['indexNum'] - 1) * 10
        return self.user_model.get_user_list_restaurant(num_offset, restaurant_id)
    
    
