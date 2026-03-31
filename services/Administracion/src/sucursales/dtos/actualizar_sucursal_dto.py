from marshmallow import Schema, fields, validate


class ActualizarSucursalDTO(Schema):
    name = fields.String(allow_none=True, validate=validate.Length(min=2, max=150))
    address = fields.String(allow_none=True, validate=validate.Length(min=5, max=500))
    phone = fields.String(allow_none=True, validate=validate.Length(max=20))
    email = fields.Email(allow_none=True)
    latitude = fields.Decimal(allow_none=True, places=8)
    longitude = fields.Decimal(allow_none=True, places=8)
    tolerance_minutes = fields.Integer(allow_none=True, validate=validate.Range(min=1, max=60))
    is_active = fields.Boolean(allow_none=True)
