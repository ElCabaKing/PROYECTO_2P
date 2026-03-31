from typing import Dict, Any
from datetime import date
from src.core.database import DataBaseHandle
from src.core.logs import HandleLogs
from .repository_interface import IPromocionRepository


class PromocionRepository(IPromocionRepository):

    def obtener_por_id(self, promocion_id: str) -> Dict[str, Any]:
        try:
            query = """
                SELECT p.id, p.sucursal_id, s.name AS sucursal_name, p.name,
                       p.description, p.discount_percentage, p.start_date, p.end_date,
                       p.is_active, p.created_at, p.updated_at
                FROM promociones p
                INNER JOIN sucursales s ON p.sucursal_id = s.id
                WHERE p.id = %s
            """
            result = DataBaseHandle.getRecords(query, 1, (promocion_id,))
            if result['result']:
                return {'result': True, 'data': result['data']}
            return {'result': False, 'data': None, 'error': result.get('message', 'Error al obtener promoción')}
        except Exception as e:
            HandleLogs.write_error("PromocionRepository.obtener_por_id", str(e))
            return {'result': False, 'data': None, 'error': str(e)}

    def obtener_por_sucursal(self, sucursal_id: str) -> Dict[str, Any]:
        try:
            query = """
                SELECT p.id, p.sucursal_id, s.name AS sucursal_name, p.name,
                       p.description, p.discount_percentage, p.start_date, p.end_date,
                       p.is_active, p.created_at, p.updated_at
                FROM promociones p
                INNER JOIN sucursales s ON p.sucursal_id = s.id
                WHERE p.sucursal_id = %s
                ORDER BY p.created_at DESC
            """
            result = DataBaseHandle.getRecords(query, 0, (sucursal_id,))
            if result['result']:
                return {'result': True, 'data': result['data'] if result['data'] else []}
            return {'result': False, 'data': [], 'error': result.get('message', 'Error al obtener promociones')}
        except Exception as e:
            HandleLogs.write_error("PromocionRepository.obtener_por_sucursal", str(e))
            return {'result': False, 'data': [], 'error': str(e)}

    def obtener_activas_por_sucursal(self, sucursal_id: str) -> Dict[str, Any]:
        try:
            hoy = date.today()
            query = """
                SELECT p.id, p.sucursal_id, s.name AS sucursal_name, p.name,
                       p.description, p.discount_percentage, p.start_date, p.end_date,
                       p.is_active, p.created_at, p.updated_at
                FROM promociones p
                INNER JOIN sucursales s ON p.sucursal_id = s.id
                WHERE p.sucursal_id = %s
                  AND p.is_active = TRUE
                  AND p.start_date <= %s
                  AND p.end_date >= %s
                ORDER BY p.end_date ASC
            """
            result = DataBaseHandle.getRecords(query, 0, (sucursal_id, hoy, hoy))
            if result['result']:
                return {'result': True, 'data': result['data'] if result['data'] else []}
            return {'result': False, 'data': [], 'error': result.get('message', 'Error al obtener promociones activas')}
        except Exception as e:
            HandleLogs.write_error("PromocionRepository.obtener_activas_por_sucursal", str(e))
            return {'result': False, 'data': [], 'error': str(e)}

    def crear(self, data: dict) -> Dict[str, Any]:
        try:
            query = """
                INSERT INTO promociones
                    (sucursal_id, name, description, discount_percentage, start_date, end_date)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id, sucursal_id, name, description, discount_percentage,
                          start_date, end_date, is_active, created_at, updated_at
            """
            record = (
                str(data['sucursal_id']),
                data['name'],
                data.get('description'),
                data.get('discount_percentage'),
                data['start_date'],
                data['end_date']
            )
            result = DataBaseHandle.ExecuteNonQuery(query, record)
            if result['result'] and result['data']:
                return self.obtener_por_id(str(result['data']['id']))
            return {'result': False, 'data': None, 'error': result.get('message', 'Error al crear promoción')}
        except Exception as e:
            HandleLogs.write_error("PromocionRepository.crear", str(e))
            return {'result': False, 'data': None, 'error': str(e)}

    def actualizar(self, promocion_id: str, data: dict) -> Dict[str, Any]:
        try:
            updates = []
            values = []

            if data.get('name') is not None:
                updates.append("name = %s")
                values.append(data['name'])
            if data.get('description') is not None:
                updates.append("description = %s")
                values.append(data['description'])
            if data.get('discount_percentage') is not None:
                updates.append("discount_percentage = %s")
                values.append(data['discount_percentage'])
            if data.get('start_date') is not None:
                updates.append("start_date = %s")
                values.append(data['start_date'])
            if data.get('end_date') is not None:
                updates.append("end_date = %s")
                values.append(data['end_date'])
            if data.get('is_active') is not None:
                updates.append("is_active = %s")
                values.append(data['is_active'])

            if not updates:
                return self.obtener_por_id(promocion_id)

            updates.append("updated_at = NOW()")
            values.append(promocion_id)

            query = f"""
                UPDATE promociones
                SET {', '.join(updates)}
                WHERE id = %s
                RETURNING id
            """
            result = DataBaseHandle.ExecuteNonQuery(query, tuple(values))
            if result['result']:
                return self.obtener_por_id(promocion_id)
            return {'result': False, 'data': None, 'error': result.get('message', 'Error al actualizar promoción')}
        except Exception as e:
            HandleLogs.write_error("PromocionRepository.actualizar", str(e))
            return {'result': False, 'data': None, 'error': str(e)}

    def eliminar(self, promocion_id: str) -> Dict[str, Any]:
        """Delete a promotion."""
        try:
            query = """
                DELETE FROM promociones
                WHERE id = %s
                RETURNING id
            """
            result = DataBaseHandle.ExecuteNonQuery(query, (promocion_id,))
            if result['result']:
                return {'result': True, 'data': True}
            return {'result': False, 'data': False, 'error': result.get('message', 'Promoción no encontrada')}
        except Exception as e:
            HandleLogs.write_error("PromocionRepository.eliminar", str(e))
            return {'result': False, 'data': False, 'error': str(e)}
