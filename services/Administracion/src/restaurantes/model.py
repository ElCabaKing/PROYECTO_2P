"""Restaurante entity representation.

This module defines the table structure for reference.
Actual data is handled as dicts from psycopg2 RealDictCursor.

Table: restaurantes
Columns:
    - id: UUID (PK)
    - name: VARCHAR(150) NOT NULL
    - legal_name: VARCHAR(255)
    - tax_id: VARCHAR(50)
    - logo_url: VARCHAR(500)
    - is_active: BOOLEAN DEFAULT TRUE
    - created_at: TIMESTAMP WITH TIME ZONE
    - updated_at: TIMESTAMP WITH TIME ZONE
"""

TABLE_NAME = "restaurantes"

COLUMNS = [
    "id",
    "name",
    "legal_name",
    "tax_id",
    "logo_url",
    "is_active",
    "created_at",
    "updated_at"
]
