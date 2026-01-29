from marshmallow import Schema, fields


class SucursalResponseDTO(Schema):
    id = fields.UUID(required=True)
    restaurante_id = fields.UUID(required=True)
    restaurante_name = fields.String(allow_none=True)  # From JOIN
    name = fields.String(required=True)
    address = fields.String(required=True)
    phone = fields.String(allow_none=True)
    email = fields.String(allow_none=True)
    latitude = fields.Decimal(allow_none=True, places=8)
    longitude = fields.Decimal(allow_none=True, places=8)
    tolerance_minutes = fields.Integer(required=True)
    is_active = fields.Boolean(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
