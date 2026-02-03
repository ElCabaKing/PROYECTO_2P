from marshmallow import Schema, fields
class UpdateUserRequest(Schema):
    Nombre = fields.String()
    Apellido = fields.String()
    Correo = fields.String()
    RoleId = fields.Integer()
    SucursalId = fields.Integer()
    
    class Meta:
        unknown = 'EXCLUDE'
        
