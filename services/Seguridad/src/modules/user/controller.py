from .services import UserService
from flask import request, jsonify, g
from src.modules.user.schemas.newUserRequest import NewUserRequest
from src.modules.user.schemas.userListRequest import UserListRequest

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
                if g.sucursal_id is not None:
                        return self.user_service.fetch_user_list(index_num,g.sucursal_id)
                return self.user_service.fetch_user_list(index_num,g.restauran_id)
        
        
