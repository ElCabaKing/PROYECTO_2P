from marshmallow import Schema, fields


class RecoveryUserPasswordRequest(Schema):
    correo = fields.String(required=True)
