from marshmallow import Schema, fields, validate
class NewUserRequest(Schema):
    cedula = fields.String(required=True,
                           validate=validate.Regexp(
                               r'^\d{8,10}$',
                               error='Cedula invalida'
                           ))
    nombre = fields.String(required=True)
    apellido = fields.String(required=True)
    correo = fields.String(required=True, 
                           validate=validate.Email(
                               error='Correo invalido'
                           ))
    contrasena = fields.String(allow_none=True,
                            )
    role_id = fields.Integer(required=True)
    sucursal_id = fields.Integer(allow_none=True)
    
    class Meta:
        unknown = 'EXCLUDE'
        
