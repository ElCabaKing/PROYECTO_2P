from marshmallow import Schema, fields, validate


class CrearRestauranteDTO(Schema):
    name = fields.String(required=True, validate=validate.Length(min=2, max=150))
    legal_name = fields.String(allow_none=True, load_default=None)
    tax_id = fields.String(allow_none=True, load_default=None)
    logo_url = fields.String(allow_none=True, load_default=None)
