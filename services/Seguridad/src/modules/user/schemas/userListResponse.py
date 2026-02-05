from marshmallow import Schema, fields
class UserListResponse(Schema):
    user_list = fields.List()