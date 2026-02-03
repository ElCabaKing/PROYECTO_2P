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
        """
        Actualiza un usuario con validación de roles.
        Si se asciende a DIRECTOR, se elimina sucursal_id
        Si se desciende DE DIRECTOR, se requiere sucursal_id
        """
        # Obtener usuario actual
        current_user = self.user_model.get_user_by_id(user_id)
        if not current_user:
            raise AppError("Usuario no encontrado", 404)
        
        # Validar lógica de sucursal según role
        new_role_id = update_data.get('role_id', current_user['role_id'])
        new_sucursal_id = update_data.get('sucursal_id', current_user['sucursal_id'])
        
        # Si es ascendido a DIRECTOR, no debe tener sucursal_id
        if new_role_id == self.DIRECTOR_ROLE_ID:
            if new_sucursal_id is not None:
                # Forzar eliminación de sucursal_id
                update_data['sucursal_id'] = None
        else:
            # Si es descendido de DIRECTOR, debe tener sucursal_id
            if current_user['role_id'] == self.DIRECTOR_ROLE_ID and new_role_id != self.DIRECTOR_ROLE_ID:
                if new_sucursal_id is None:
                    raise AppError("Un usuario no director debe tener asignada una sucursal", 400)
        
        # Ejecutar actualización
        result = self.user_model.update_user(user_id, update_data)
        return result

