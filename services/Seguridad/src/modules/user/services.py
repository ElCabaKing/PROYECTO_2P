from .model import UserModel
from bcrypt import hashpw, gensalt
from src.utils.Email_Sender import send_email
from flask import current_app
from core.exceptions import AppError
import threading


class UserService:
    
    def __init__(self):
        self.user_model = UserModel()
    
    # Constante: role_id para DIRECTOR
    DIRECTOR_ROLE_ID = 1

    def create_user(self, user):    
        password_hash = hashpw(user['contrasena'].encode(), gensalt())
        user['contrasena'] = password_hash
        response = self.user_model.insert_new_user(user)
        app = current_app._get_current_object()
        threading.Thread(
        target=send_email,
        args=(app, user['correo'],"Bienvenido","Bienvenido a nuestro equipo"),
        daemon=True
        ).start()
        return response

    def fetch_user_list(self, index_num, sucursal_id=None, restaurant_id=None):
        num_offset = (index_num['index_num'] - 1) * 10
        if sucursal_id:
            return self.user_model.get_user_list(num_offset, sucursal_id)
        elif restaurant_id:
            return self.user_model.get_user_list_restaurant(num_offset, restaurant_id)
        else:
            raise ValueError("Se requiere sucursal_id o restaurant_id")
    
    def update_user(self, user_id, update_data):
        current_user = self.user_model.get_user_by_id(user_id)
        if not current_user:
            raise AppError("Usuario no encontrado", 404)
        

        new_role_id = update_data.get('role_id', current_user['role_id'])
        new_sucursal_id = update_data.get('sucursal_id', current_user['sucursal_id'])

        if new_role_id == self.DIRECTOR_ROLE_ID:
            if new_sucursal_id is not None:
  
                update_data['sucursal_id'] = None
        else:
           
            if current_user['role_id'] == self.DIRECTOR_ROLE_ID and new_role_id != self.DIRECTOR_ROLE_ID:
                if new_sucursal_id is None:
                    raise AppError("Un usuario no director debe tener asignada una sucursal", 400)
        

        result = self.user_model.update_user(user_id, update_data)
        return result
    
    def fetch_roles(self):
        roles = self.user_model.get_all_roles()
        return roles
    
    def get_current_user(self, user_id):

        user = self.user_model.get_user_by_id(user_id)
        if not user:
            raise AppError("Usuario no encontrado", 404)
        
        return {
            "id": user['id'],
            "cedula": user['cedula'],
            "nombre": user['nombre'],
            "apellido": user['apellido'],
            "correo": user['correo'],
            "role_id": user['role_id'],
            "sucursal_id": user['sucursal_id'],
            "restaurant_id": user['restaurant_id'],
            "activo": user['activo']
        }

