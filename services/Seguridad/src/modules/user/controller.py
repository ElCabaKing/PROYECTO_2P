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
                result = self.user_service.create_user(user_data)
                return jsonify({"success": result}), 201
        
        def fetch_user_list(self):
                schema = UserListRequest()
                index_num = schema.load(request.args)
                return self.user_service.fetch_user_list(index_num,g.sucursal_id,g.restaurant_id)

        
        def update_user(self, user_id):
                try:
                        schema = UpdateUserRequest()
                        update_data = schema.load(request.json)
                        
                        result = self.user_service.update_user(user_id, update_data)
                        return jsonify({"success": result, "message": "Usuario actualizado exitosamente"}), 200
                except Exception as e:
                        return jsonify({"error": str(e)}), 400
        


