from marshmallow import Schema, fields, validate


class ActualizarMesaDTO(Schema):
    capacity_min = fields.Integer(allow_none=True, validate=validate.Range(min=1))
    capacity_max = fields.Integer(allow_none=True, validate=validate.Range(min=1))
    location = fields.String(allow_none=True, validate=validate.Length(max=100))
    description = fields.String(allow_none=True)
    is_active = fields.Boolean(allow_none=True)
