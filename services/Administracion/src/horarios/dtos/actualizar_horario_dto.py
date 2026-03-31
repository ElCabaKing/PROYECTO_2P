from marshmallow import Schema, fields, validate


class ActualizarHorarioDTO(Schema):
    day_of_week = fields.Integer(allow_none=True, validate=validate.Range(min=0, max=6))
    opening_time = fields.Time(allow_none=True, format='%H:%M')
    closing_time = fields.Time(allow_none=True, format='%H:%M')
    is_active = fields.Boolean(allow_none=True)
