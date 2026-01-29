from marshmallow import Schema, fields, validate


class ActualizarRestauranteDTO(Schema):
    name = fields.String(allow_none=True, validate=validate.Length(min=2, max=150))
    legal_name = fields.String(allow_none=True)
    tax_id = fields.String(allow_none=True)
    logo_url = fields.String(allow_none=True)
    is_active = fields.Boolean(allow_none=True)
