from marshmallow import Schema, fields
class UserPayload(Schema):
    cedula = fields.String(required=True)
    nombre = fields.String(required=True)
    apellido = fields.String(required=True)
    correo = fields.String(required=True)
    role_id = fields.Integer(required=True)
    sucursal_id = fields.Integer(required=True)