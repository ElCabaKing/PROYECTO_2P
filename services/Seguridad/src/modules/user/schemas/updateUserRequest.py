from marshmallow import Schema, fields
class UpdateUserRequest(Schema):
    nombre = fields.String()
    apellido = fields.String()
    correo = fields.String()
    role_id = fields.Integer()
    sucursal_id = fields.Integer()
    
    class Meta:
        unknown = 'EXCLUDE'
        
