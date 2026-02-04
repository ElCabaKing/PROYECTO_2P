from marshmallow import Schema, fields, validate

class UpdatePasswordRequest(Schema):
    new_password = fields.String(required=True,
                               validate=validate.Length(
                                   min=8,
                                   error='La contraseña debe tener al menos 8 caracteres'
                               )
                            )
    confirm_password = fields.String(required=True,
                               validate=validate.Length(
                                   min=8,
                                   error='La contraseña debe tener al menos 8 caracteres'
                               )
                            )
    token = fields.String(required=True)