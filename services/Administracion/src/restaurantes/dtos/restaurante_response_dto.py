from marshmallow import Schema, fields


class RestauranteResponseDTO(Schema):
    id = fields.UUID(required=True)
    name = fields.String(required=True)
    legal_name = fields.String(allow_none=True)
    tax_id = fields.String(allow_none=True)
    logo_url = fields.String(allow_none=True)
    is_active = fields.Boolean(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
