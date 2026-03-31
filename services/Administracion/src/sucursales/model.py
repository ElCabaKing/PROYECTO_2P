"""Sucursal entity representation.

This module defines the table structure for reference.
Actual data is handled as dicts from psycopg2 RealDictCursor.

Table: sucursales
Columns:
    - id: UUID (PK)
    - restaurante_id: UUID (FK -> restaurantes.id)
    - name: VARCHAR(150) NOT NULL
    - address: VARCHAR(500) NOT NULL
    - phone: VARCHAR(20)
    - email: VARCHAR(255)
    - latitude: DECIMAL(10,8)
    - longitude: DECIMAL(11,8)
    - tolerance_minutes: INTEGER DEFAULT 15
    - is_active: BOOLEAN DEFAULT TRUE
    - created_at: TIMESTAMP WITH TIME ZONE
    - updated_at: TIMESTAMP WITH TIME ZONE
"""

TABLE_NAME = "sucursales"

COLUMNS = [
    "id",
    "restaurante_id",
    "name",
    "address",
    "phone",
    "email",
    "latitude",
    "longitude",
    "tolerance_minutes",
    "is_active",
    "created_at",
    "updated_at"
]
