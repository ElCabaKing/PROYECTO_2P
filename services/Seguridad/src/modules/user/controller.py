from .services import UserService
from flask import request, jsonify, g
from src.modules.user.schemas.newUserRequest import NewUserRequest
from src.modules.user.schemas.userListRequest import UserListRequest
from src.modules.user.schemas.updateUserRequest import UpdateUserRequest

class UserController:

        def __init__(self):
                self.user_service = UserService()


        def new_user(self):
                schema = NewUserRequest()
                user_data = schema.load(request.json)
                result = self.user_service.create_user(user_data,g.restaurant_id)
                return jsonify({"success": result}), 201
        
        def fetch_user_list(self):
                schema = UserListRequest()
                index_num = schema.load(request.args)
                return self.user_service.fetch_user_list(g.role, index_num, g.sucursal_id, g.restaurant_id)

        
        def update_user(self, user_id):
                try:
                        schema = UpdateUserRequest()
                        update_data = schema.load(request.json)
                        
                        result = self.user_service.update_user(user_id, update_data)
                        return jsonify({"success": result, "message": "Usuario actualizado exitosamente"}), 200
                except Exception as e:
                        return jsonify({"error": str(e)}), 400
        
        def fetch_roles(self):
                try:
                        roles = self.user_service.fetch_roles()
                        return jsonify({"roles": roles}), 200
                except Exception as e:
                        return jsonify({"error": str(e)}), 500
        
        def get_current_user(self):
                try:
                        user = self.user_service.get_current_user(g.user_id)
                        return jsonify({"user": user}), 200
                except Exception as e:
                        return jsonify({"error": str(e)}), 500
        
        def get_user_by_id(self, user_id):
                try:
                        user = self.user_service.get_user_by_id(user_id, g.role, g.sucursal_id, g.restaurant_id)
                        return jsonify({"user": user}), 200
                except Exception as e:
                        return jsonify({"error": str(e)}), 500


        def fetch_roles_and_branches(self):
                try:
                        data = self.user_service.fetch_roles_and_branches(g.restaurant_id)
                        return jsonify(data), 200
                except Exception as e:
                        return jsonify({"error": str(e)}), 500
