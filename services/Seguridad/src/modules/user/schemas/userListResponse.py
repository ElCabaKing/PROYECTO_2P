from marshmallow import Schema, fields
class UserListResponse(Schema):
    UserList = fields.List()