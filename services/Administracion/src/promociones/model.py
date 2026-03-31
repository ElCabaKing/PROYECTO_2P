"""
Promocion Model Reference

Table: promociones
Columns:
    - id: UUID (PK)
    - sucursal_id: UUID (FK -> sucursales.id)
    - name: VARCHAR(150) NOT NULL
    - description: TEXT
    - discount_percentage: NUMERIC(5,2)
    - start_date: DATE NOT NULL
    - end_date: DATE NOT NULL
    - is_active: BOOLEAN DEFAULT TRUE
    - created_at: TIMESTAMPTZ
    - updated_at: TIMESTAMPTZ

Relationships:
    - sucursal: Many-to-One with sucursales
"""

TABLE_NAME = "promociones"
COLUMNS = [
    "id", "sucursal_id", "name", "description", "discount_percentage",
    "start_date", "end_date", "is_active", "created_at", "updated_at"
]
