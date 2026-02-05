from marshmallow import Schema, fields


class PromocionResponseDTO(Schema):
    id = fields.Int(dump_only=True)
    sucursal_id = fields.Int(dump_only=True)
    sucursal_name = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    description = fields.Str(dump_only=True, allow_none=True)
    discount_percentage = fields.Decimal(dump_only=True, as_string=True, allow_none=True)
    start_date = fields.Date(dump_only=True)
    end_date = fields.Date(dump_only=True)
    is_active = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
