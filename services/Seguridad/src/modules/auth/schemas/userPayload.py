from marshmallow import Schema, fields
class UserPayload(Schema):
    Cedula = fields.String(required=True)
    Nombre = fields.String(required=True)
    Apellido = fields.String(required=True)
    Correo = fields.String(required=True)
    RoleId = fields.Integer(required=True)
    SucursalId = fields.Integer(required=True)