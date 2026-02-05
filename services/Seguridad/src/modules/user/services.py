from .model import UserModel
from bcrypt import hashpw, gensalt
from src.utils.Email_Sender import send_email
from flask import current_app
from core.exceptions import AppError
import threading
import math
import secrets
import string


class UserService:
    
    def __init__(self):
        self.user_model = UserModel()
    
    # Constantes de roles
    DIRECTOR_ROLE_ID = 1
    ADMIN_ROLE_ID = 2
    EMPLOYEE_ROLE_ID = 3
    
    # Constante para contrasenas
    caracteres = string.ascii_letters + string.digits

    def create_user(self, user, restaurant_id):    
        temp_password = ''.join(secrets.choice(self.caracteres) for _ in range(10))
        password_hash = hashpw(temp_password.encode(), gensalt())
        user['contrasena'] = password_hash
        response = self.user_model.insert_new_user(user, restaurant_id)
        app = current_app._get_current_object()
        threading.Thread(
        target=send_email,
        args=(app, user['correo'],f"""Bienvenido a nuestro equipo
              Puedes ingresar usando tu cedula con la contrasena {temp_password}
              link= https//localhost:3000/""",
              "Bienvenido"),
        daemon=True
        ).start()
        return response

    def fetch_user_list(self, user_role, index_num, sucursal_id=None, restaurant_id=None):

        # Validar que solo Director y Administrador puedan acceder
        if user_role == self.EMPLOYEE_ROLE_ID:
            raise AppError("Empleados no tienen permiso para ver la lista de usuarios")
        
        num_offset = (index_num['index_num'] - 1) * 6
        
        # Director ve todo el restaurante
        if user_role == self.DIRECTOR_ROLE_ID and restaurant_id:
            users = self.user_model.get_user_list_restaurant(num_offset, restaurant_id)
            total = self.user_model.get_user_count_restaurant(restaurant_id)
            max_index = math.ceil(total / 6)
            return {"users": users, "max_index": max_index}
        
        # Administrador ve su sucursal
        if user_role == self.ADMIN_ROLE_ID and sucursal_id:
            users = self.user_model.get_user_list(num_offset, sucursal_id)
            total = self.user_model.get_user_count(sucursal_id)
            max_index = math.ceil(total / 6)
            return {"users": users, "max_index": max_index}
        
        raise AppError("Parámetros inválidos para obtener lista de usuarios")
    
    def update_user(self, user_id, update_data):
        current_user = self.user_model.get_user_by_id(user_id)
        if not current_user:
            raise AppError("Usuario no encontrado")
        

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
        
        # Obtener menús disponibles del usuario según su rol
        menus = self.user_model.get_menus_by_role(user['role_id'])
        
        return {
            "id": user['id'],
            "cedula": user['cedula'],
            "nombre": user['nombre'],
            "apellido": user['apellido'],
            "correo": user['correo'],
            "role_id": user['role_id'],
            "sucursal_id": user['sucursal_id'],
            "restaurant_id": user['restaurante_id'],
            "activo": user['is_active'],
            "menus": menus
        }
    
    def get_user_by_id(self, requested_user_id, requester_role, requester_sucursal_id, requester_restaurant_id):

        if requester_role == self.EMPLOYEE_ROLE_ID:
            raise AppError("Empleados no tienen permiso para ver datos de otros usuarios")
        

        target_user = self.user_model.get_user_by_id(requested_user_id)
        if not target_user:
            raise AppError("Usuario no encontrado")
        
       
        if requester_role == self.DIRECTOR_ROLE_ID:
            if target_user['restaurant_id'] != requester_restaurant_id:
                raise AppError("No tienes permiso para ver este usuario")
        
        if requester_role == self.ADMIN_ROLE_ID:
            if target_user['sucursal_id'] != requester_sucursal_id:
                raise AppError("No tienes permiso para ver este usuario")
        
        return {
            "id": target_user['id'],
            "cedula": target_user['cedula'],
            "nombre": target_user['nombre'],
            "apellido": target_user['apellido'],
            "correo": target_user['correo'],
            "role_id": target_user['role_id'],
            "sucursal_id": target_user['sucursal_id'],
            "restaurant_id": target_user['restaurant_id'],
            "activo": target_user['activo']
        }

    def fetch_roles_and_branches(self, restaurant_id):
            """Obtiene los roles y las sucursales de un restaurante"""
            roles = self.user_model.get_all_roles()
            branches = self.user_model.get_branches_by_restaurant(restaurant_id)
            
            return {
                "roles": roles,
                "branches": branches
            }