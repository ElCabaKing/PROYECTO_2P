from marshmallow import Schema, fields, validate, validates, validates_schema, ValidationError


class CrearPromocionDTO(Schema):
    sucursal_id = fields.UUID(required=True)
    name = fields.Str(required=True, validate=validate.Length(min=3, max=150))
    description = fields.Str(allow_none=True, load_default=None)
    discount_percentage = fields.Decimal(places=2, allow_none=True, load_default=None)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)

    @validates('name')
    def validar_nombre(self, value):
        if len(value.strip()) < 3:
            raise ValidationError('El nombre debe tener al menos 3 caracteres')
        return value.strip()

    @validates_schema
    def validar_fechas(self, data, **kwargs):
        if 'start_date' in data and 'end_date' in data:
            if data['end_date'] < data['start_date']:
                raise ValidationError('end_date debe ser posterior a start_date', field_name='end_date')
