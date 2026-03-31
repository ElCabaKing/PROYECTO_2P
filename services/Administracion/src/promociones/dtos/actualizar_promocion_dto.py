from marshmallow import Schema, fields, validate, validates_schema, ValidationError


class ActualizarPromocionDTO(Schema):
    name = fields.Str(validate=validate.Length(min=3, max=150), load_default=None)
    description = fields.Str(allow_none=True, load_default=None)
    discount_percentage = fields.Decimal(places=2, allow_none=True, load_default=None)
    start_date = fields.Date(load_default=None)
    end_date = fields.Date(load_default=None)
    is_active = fields.Bool(load_default=None)

    @validates_schema
    def validar_fechas(self, data, **kwargs):
        if data.get('start_date') and data.get('end_date'):
            if data['end_date'] < data['start_date']:
                raise ValidationError('end_date debe ser posterior a start_date', field_name='end_date')
