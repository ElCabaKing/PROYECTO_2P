from marshmallow import Schema, fields


class UserListRequest(Schema):
    index_num= fields.Integer(required=True)