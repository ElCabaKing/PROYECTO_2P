from marshmallow import Schema, fields


class HorarioResponseDTO(Schema):
    id = fields.Int(required=True)
    sucursal_id = fields.Int(required=True)
    sucursal_name = fields.String(allow_none=True)  # From JOIN
    day_of_week = fields.Integer(required=True)
    day_name = fields.String(allow_none=True)  # Computed field
    opening_time = fields.Time(required=True, format='%H:%M')
    closing_time = fields.Time(required=True, format='%H:%M')
    is_active = fields.Boolean(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
