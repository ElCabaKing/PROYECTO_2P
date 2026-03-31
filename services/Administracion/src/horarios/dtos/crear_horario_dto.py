from marshmallow import Schema, fields, validate


class CrearHorarioDTO(Schema):
    sucursal_id = fields.UUID(required=True)
    day_of_week = fields.Integer(required=True, validate=validate.Range(min=0, max=6))
    opening_time = fields.Time(required=True, format='%H:%M')
    closing_time = fields.Time(required=True, format='%H:%M')
