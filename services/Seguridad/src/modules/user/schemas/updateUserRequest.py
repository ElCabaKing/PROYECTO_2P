from marshmallow import Schema, fields, validate

class UpdateUserRequest(Schema):
    nombre = fields.String(allow_none=True)
    apellido = fields.String(allow_none=True)
    correo = fields.String(allow_none=True)
    role_id = fields.Integer(allow_none=True)
    sucursal_id = fields.Integer(allow_none=True)
    
    class Meta:
        unknown = 'EXCLUDE'

