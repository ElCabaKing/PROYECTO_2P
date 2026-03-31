from marshmallow import Schema, fields


class MesaResponseDTO(Schema):
    id = fields.UUID(required=True)
    sucursal_id = fields.UUID(required=True)
    sucursal_name = fields.String(allow_none=True)  # From JOIN
    table_number = fields.String(required=True)
    capacity_min = fields.Integer(required=True)
    capacity_max = fields.Integer(required=True)
    location = fields.String(allow_none=True)
    description = fields.String(allow_none=True)
    is_active = fields.Boolean(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
