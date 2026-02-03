from marshmallow import Schema, fields

class UpdatePasswordRequest(Schema):
    new_password = fields.String(required=True)
    confirm_password = fields.String(required=True)
    token = fields.String(required=True)