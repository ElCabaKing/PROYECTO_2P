"""Mesa entity representation.

This module defines the table structure for reference.
Actual data is handled as dicts from psycopg2 RealDictCursor.

Table: mesas
Columns:
    - id: UUID (PK)
    - sucursal_id: UUID (FK -> sucursales.id)
    - table_number: VARCHAR(20) NOT NULL
    - capacity_min: INTEGER DEFAULT 1
    - capacity_max: INTEGER NOT NULL
    - location: VARCHAR(100)
    - description: TEXT
    - is_active: BOOLEAN DEFAULT TRUE
    - created_at: TIMESTAMP WITH TIME ZONE
    - updated_at: TIMESTAMP WITH TIME ZONE
"""

TABLE_NAME = "mesas"

COLUMNS = [
    "id",
    "sucursal_id",
    "table_number",
    "capacity_min",
    "capacity_max",
    "location",
    "description",
    "is_active",
    "created_at",
    "updated_at"
]
