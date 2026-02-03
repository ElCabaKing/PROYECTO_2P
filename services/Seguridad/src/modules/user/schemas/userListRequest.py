from marshmallow import Schema, fields


class UserListRequest(Schema):
    indexNum= fields.Integer(required=True)