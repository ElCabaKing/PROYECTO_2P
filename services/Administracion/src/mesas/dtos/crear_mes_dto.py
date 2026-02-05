from marshmallow import Schema, fields, validate, validates_schema, ValidationError


class CrearMesaDTO(Schema):
    sucursal_id = fields.Int(required=True)
    capacity_min = fields.Integer(load_default=1, validate=validate.Range(min=1))
    capacity_max = fields.Integer(required=True, validate=validate.Range(min=1))
    table_number = fields.String(required=True)
    location = fields.String(allow_none=True, load_default=None, validate=validate.Length(max=100))
    description = fields.String(allow_none=True, load_default=None)

    @validates_schema
    def validate_capacity(self, data, **kwargs):
        if data.get('capacity_max', 0) < data.get('capacity_min', 1):
            raise ValidationError('capacity_max debe ser >= capacity_min')
