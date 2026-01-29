"""Horario entity representation.

This module defines the table structure for reference.
Actual data is handled as dicts from psycopg2 RealDictCursor.

Table: horarios
Columns:
    - id: UUID (PK)
    - sucursal_id: UUID (FK -> sucursales.id)
    - day_of_week: INTEGER NOT NULL (0=Domingo, 6=Sábado)
    - opening_time: TIME NOT NULL
    - closing_time: TIME NOT NULL
    - is_active: BOOLEAN DEFAULT TRUE
    - created_at: TIMESTAMP WITH TIME ZONE
    - updated_at: TIMESTAMP WITH TIME ZONE
"""

TABLE_NAME = "horarios"

COLUMNS = [
    "id",
    "sucursal_id",
    "day_of_week",
    "opening_time",
    "closing_time",
    "is_active",
    "created_at",
    "updated_at"
]

DAYS_OF_WEEK = {
    0: "Domingo",
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado"
}
