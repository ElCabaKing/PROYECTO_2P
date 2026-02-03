from marshmallow import Schema, fields, validate
class NewUserRequest(Schema):
    Cedula = fields.String(required=True,
                           validate=validate.Regexp(
                               r'^\d{8,10}$',
                               error='Cedula invalida'
                           ))
    Nombre = fields.String(required=True)
    Apellido = fields.String(required=True)
    Correo = fields.String(required=True)
    Contrasena = fields.String(required=True,
                               validate=validate.Length(
                                   min=8,
                                   error='La contraseña debe tener al menos 8 caracteres'
                               )
                            )
    RoleId = fields.Integer(required=True)
    SucursalId = fields.Integer(required=True)
