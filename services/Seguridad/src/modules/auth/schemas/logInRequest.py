from marshmallow import Schema, fields


class LogInRequest(Schema):
    Cedula = fields.String(required=True)
    Contrasena = fields.String(required=True)