from marshmallow import Schema, fields, validate


class CrearSucursalDTO(Schema):
    restaurante_id = fields.Int(required=True)
    name = fields.String(required=True, validate=validate.Length(min=2, max=150))
    address = fields.String(required=True, validate=validate.Length(min=5, max=500))
    phone = fields.String(allow_none=True, load_default=None, validate=validate.Length(max=20))
    email = fields.Email(allow_none=True, load_default=None)
    latitude = fields.Decimal(allow_none=True, load_default=None, places=8)
    longitude = fields.Decimal(allow_none=True, load_default=None, places=8)
    tolerance_minutes = fields.Integer(load_default=15, validate=validate.Range(min=1, max=60))
