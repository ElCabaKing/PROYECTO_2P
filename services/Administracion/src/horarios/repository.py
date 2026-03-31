from typing import Dict, Any
from src.core.database import DataBaseHandle
from src.shared.response import internal_response
from .repository_interface import IHorarioRepository
from .model import DAYS_OF_WEEK


class HorarioRepository(IHorarioRepository):
    """Repository for Horario using raw SQL with psycopg2."""

    def _add_day_name(self, data):
        if data is None:
            return None
        if isinstance(data, list):
            for item in data:
                if item and 'day_of_week' in item:
                    item['day_name'] = DAYS_OF_WEEK.get(item['day_of_week'], '')
        elif isinstance(data, dict) and 'day_of_week' in data:
            data['day_name'] = DAYS_OF_WEEK.get(data['day_of_week'], '')
        return data

    def obtener_por_id(self, horario_id: str) -> Dict[str, Any]:
        query = """
            SELECT h.id, h.sucursal_id, s.name AS sucursal_name,
                   h.day_of_week, h.opening_time, h.closing_time,
                   h.is_active, h.created_at, h.updated_at
            FROM horarios h
            INNER JOIN sucursales s ON h.sucursal_id = s.id
            WHERE h.id = %s
        """
        result = DataBaseHandle.getRecords(query, 1, (horario_id,))
        if result['result'] and result['data']:
            result['data'] = self._add_day_name(result['data'])
        return result

    def obtener_por_sucursal(self, sucursal_id: str) -> Dict[str, Any]:
        query = """
            SELECT h.id, h.sucursal_id, s.name AS sucursal_name,
                   h.day_of_week, h.opening_time, h.closing_time,
                   h.is_active, h.created_at, h.updated_at
            FROM horarios h
            INNER JOIN sucursales s ON h.sucursal_id = s.id
            WHERE h.sucursal_id = %s
            ORDER BY h.day_of_week
        """
        result = DataBaseHandle.getRecords(query, 0, (sucursal_id,))
        if result['result'] and result['data']:
            result['data'] = self._add_day_name(result['data'])
        return result

    def obtener_por_sucursal_y_dia(self, sucursal_id: str, day_of_week: int) -> Dict[str, Any]:
        query = """
            SELECT h.id, h.sucursal_id, s.name AS sucursal_name,
                   h.day_of_week, h.opening_time, h.closing_time,
                   h.is_active, h.created_at, h.updated_at
            FROM horarios h
            INNER JOIN sucursales s ON h.sucursal_id = s.id
            WHERE h.sucursal_id = %s AND h.day_of_week = %s
        """
        result = DataBaseHandle.getRecords(query, 1, (sucursal_id, day_of_week))
        if result['result'] and result['data']:
            result['data'] = self._add_day_name(result['data'])
        return result

    def crear(self, data: dict) -> Dict[str, Any]:
        query = """
            INSERT INTO horarios
                (sucursal_id, day_of_week, opening_time, closing_time)
            VALUES (%s, %s, %s, %s)
            RETURNING id, sucursal_id, day_of_week, opening_time, closing_time,
                      is_active, created_at, updated_at
        """
        record = (
            str(data.get('sucursal_id')),
            data.get('day_of_week'),
            data.get('opening_time'),
            data.get('closing_time')
        )
        result = DataBaseHandle.ExecuteNonQuery(query, record)
        if result['result'] and result['data']:
            result['data'] = self._add_day_name(result['data'])
        return result

    def actualizar(self, horario_id: str, data: dict) -> Dict[str, Any]:
        fields_to_update = []
        values = []

        if 'day_of_week' in data and data['day_of_week'] is not None:
            fields_to_update.append("day_of_week = %s")
            values.append(data['day_of_week'])
        if 'opening_time' in data and data['opening_time'] is not None:
            fields_to_update.append("opening_time = %s")
            values.append(data['opening_time'])
        if 'closing_time' in data and data['closing_time'] is not None:
            fields_to_update.append("closing_time = %s")
            values.append(data['closing_time'])
        if 'is_active' in data and data['is_active'] is not None:
            fields_to_update.append("is_active = %s")
            values.append(data['is_active'])

        if not fields_to_update:
            return internal_response(False, None, "No hay campos para actualizar")

        values.append(horario_id)
        query = f"""
            UPDATE horarios
            SET {', '.join(fields_to_update)}, updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
            RETURNING id, sucursal_id, day_of_week, opening_time, closing_time,
                      is_active, created_at, updated_at
        """
        result = DataBaseHandle.ExecuteNonQuery(query, tuple(values))
        if result['result'] and result['data']:
            result['data'] = self._add_day_name(result['data'])
        return result

    def eliminar(self, horario_id: str) -> Dict[str, Any]:
        query = """
            DELETE FROM horarios
            WHERE id = %s
        """
        return DataBaseHandle.ExecuteNonQuery(query, (horario_id,))
