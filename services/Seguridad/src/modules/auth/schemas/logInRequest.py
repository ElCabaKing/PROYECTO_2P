from marshmallow import Schema, fields


class LogInRequest(Schema):
    cedula = fields.String(required=True)
    contrasena = fields.String(required=True)