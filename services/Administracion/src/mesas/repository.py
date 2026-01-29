from typing import Dict, Any
from src.core.database import DataBaseHandle
from src.shared.response import internal_response
from .repository_interface import IMesaRepository


class MesaRepository(IMesaRepository):

    def obtener_por_id(self, mesa_id: str) -> Dict[str, Any]:
        query = """
            SELECT m.id, m.sucursal_id, s.name AS sucursal_name,
                   m.table_number, m.capacity_min, m.capacity_max,
                   m.location, m.description, m.is_active,
                   m.created_at, m.updated_at
            FROM mesas m
            INNER JOIN sucursales s ON m.sucursal_id = s.id
            WHERE m.id = %s
        """
        return DataBaseHandle.getRecords(query, 1, (mesa_id,))

    def obtener_todos(self) -> Dict[str, Any]:
        query = """
            SELECT m.id, m.sucursal_id, s.name AS sucursal_name,
                   m.table_number, m.capacity_min, m.capacity_max,
                   m.location, m.description, m.is_active,
                   m.created_at, m.updated_at
            FROM mesas m
            INNER JOIN sucursales s ON m.sucursal_id = s.id
            ORDER BY s.name, m.table_number
        """
        return DataBaseHandle.getRecords(query, 0)

    def obtener_por_sucursal(self, sucursal_id: str) -> Dict[str, Any]:
        query = """
            SELECT m.id, m.sucursal_id, s.name AS sucursal_name,
                   m.table_number, m.capacity_min, m.capacity_max,
                   m.location, m.description, m.is_active,
                   m.created_at, m.updated_at
            FROM mesas m
            INNER JOIN sucursales s ON m.sucursal_id = s.id
            WHERE m.sucursal_id = %s
            ORDER BY m.table_number
        """
        return DataBaseHandle.getRecords(query, 0, (sucursal_id,))

    def obtener_disponibles_por_capacidad(self, sucursal_id: str, num_personas: int) -> Dict[str, Any]:
        query = """
            SELECT m.id, m.sucursal_id, s.name AS sucursal_name,
                   m.table_number, m.capacity_min, m.capacity_max,
                   m.location, m.description, m.is_active,
                   m.created_at, m.updated_at
            FROM mesas m
            INNER JOIN sucursales s ON m.sucursal_id = s.id
            WHERE m.sucursal_id = %s
              AND m.is_active = TRUE
              AND m.capacity_min <= %s
              AND m.capacity_max >= %s
            ORDER BY m.capacity_max, m.table_number
        """
        return DataBaseHandle.getRecords(query, 0, (sucursal_id, num_personas, num_personas))

    def obtener_siguiente_numero_mesa(self, sucursal_id: str) -> Dict[str, Any]:
        query = """
            SELECT COUNT(*) + 1 AS next_number
            FROM mesas
            WHERE sucursal_id = %s
        """
        return DataBaseHandle.getRecords(query, 1, (sucursal_id,))

    def crear(self, data: dict) -> Dict[str, Any]:
        query = """
            INSERT INTO mesas
                (sucursal_id, table_number, capacity_min, capacity_max, location, description)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id, sucursal_id, table_number, capacity_min, capacity_max,
                      location, description, is_active, created_at, updated_at
        """
        record = (
            str(data.get('sucursal_id')),
            data.get('table_number'),
            data.get('capacity_min', 1),
            data.get('capacity_max'),
            data.get('location'),
            data.get('description')
        )
        return DataBaseHandle.ExecuteNonQuery(query, record)

    def actualizar(self, mesa_id: str, data: dict) -> Dict[str, Any]:
        fields_to_update = []
        values = []

        if 'capacity_min' in data and data['capacity_min'] is not None:
            fields_to_update.append("capacity_min = %s")
            values.append(data['capacity_min'])
        if 'capacity_max' in data and data['capacity_max'] is not None:
            fields_to_update.append("capacity_max = %s")
            values.append(data['capacity_max'])
        if 'location' in data:
            fields_to_update.append("location = %s")
            values.append(data['location'])
        if 'description' in data:
            fields_to_update.append("description = %s")
            values.append(data['description'])
        if 'is_active' in data and data['is_active'] is not None:
            fields_to_update.append("is_active = %s")
            values.append(data['is_active'])

        if not fields_to_update:
            return internal_response(False, None, "No hay campos para actualizar")

        values.append(mesa_id)
        query = f"""
            UPDATE mesas
            SET {', '.join(fields_to_update)}, updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
            RETURNING id, sucursal_id, table_number, capacity_min, capacity_max,
                      location, description, is_active, created_at, updated_at
        """
        return DataBaseHandle.ExecuteNonQuery(query, tuple(values))

    def eliminar(self, mesa_id: str) -> Dict[str, Any]:
        query = """
            DELETE FROM mesas
            WHERE id = %s
        """
        return DataBaseHandle.ExecuteNonQuery(query, (mesa_id,))
