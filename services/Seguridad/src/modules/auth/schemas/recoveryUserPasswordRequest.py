from marshmallow import Schema, fields


class RecoveryUserPasswordRequest(Schema):
    Correo = fields.String(required=True)
