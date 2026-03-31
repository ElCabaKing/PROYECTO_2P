from typing import Dict, Any
from src.core.database import DataBaseHandle
from src.shared.response import internal_response
from .repository_interface import ISucursalRepository


class SucursalRepository(ISucursalRepository):

    def obtener_por_id(self, sucursal_id: str) -> Dict[str, Any]:
        query = """
            SELECT s.id, s.restaurante_id, r.name AS restaurante_name,
                   s.name, s.address, s.phone, s.email,
                   s.latitude, s.longitude, s.tolerance_minutes,
                   s.is_active, s.created_at, s.updated_at
            FROM sucursales s
            INNER JOIN restaurantes r ON s.restaurante_id = r.id
            WHERE s.id = %s
        """
        return DataBaseHandle.getRecords(query, 1, (sucursal_id,))

    def obtener_todos(self) -> Dict[str, Any]:
        query = """
            SELECT s.id, s.restaurante_id, r.name AS restaurante_name,
                   s.name, s.address, s.phone, s.email,
                   s.latitude, s.longitude, s.tolerance_minutes,
                   s.is_active, s.created_at, s.updated_at
            FROM sucursales s
            INNER JOIN restaurantes r ON s.restaurante_id = r.id
            ORDER BY r.name, s.name
        """
        return DataBaseHandle.getRecords(query, 0)

    def obtener_por_restaurante(self, restaurante_id: str) -> Dict[str, Any]:
        query = """
            SELECT s.id, s.restaurante_id, r.name AS restaurante_name,
                   s.name, s.address, s.phone, s.email,
                   s.latitude, s.longitude, s.tolerance_minutes,
                   s.is_active, s.created_at, s.updated_at
            FROM sucursales s
            INNER JOIN restaurantes r ON s.restaurante_id = r.id
            WHERE s.restaurante_id = %s
            ORDER BY s.name
        """
        return DataBaseHandle.getRecords(query, 0, (restaurante_id,))

    def crear(self, data: dict) -> Dict[str, Any]:
        query = """
            INSERT INTO sucursales
                (restaurante_id, name, address, phone, email, latitude, longitude, tolerance_minutes)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id, restaurante_id, name, address, phone, email,
                      latitude, longitude, tolerance_minutes, is_active, created_at, updated_at
        """
        record = (
            str(data.get('restaurante_id')),
            data.get('name'),
            data.get('address'),
            data.get('phone'),
            data.get('email'),
            data.get('latitude'),
            data.get('longitude'),
            data.get('tolerance_minutes', 15)
        )
        return DataBaseHandle.ExecuteNonQuery(query, record)

    def actualizar(self, sucursal_id: str, data: dict) -> Dict[str, Any]:
        fields_to_update = []
        values = []

        if 'name' in data and data['name'] is not None:
            fields_to_update.append("name = %s")
            values.append(data['name'])
        if 'address' in data and data['address'] is not None:
            fields_to_update.append("address = %s")
            values.append(data['address'])
        if 'phone' in data:
            fields_to_update.append("phone = %s")
            values.append(data['phone'])
        if 'email' in data:
            fields_to_update.append("email = %s")
            values.append(data['email'])
        if 'latitude' in data:
            fields_to_update.append("latitude = %s")
            values.append(data['latitude'])
        if 'longitude' in data:
            fields_to_update.append("longitude = %s")
            values.append(data['longitude'])
        if 'tolerance_minutes' in data and data['tolerance_minutes'] is not None:
            fields_to_update.append("tolerance_minutes = %s")
            values.append(data['tolerance_minutes'])
        if 'is_active' in data and data['is_active'] is not None:
            fields_to_update.append("is_active = %s")
            values.append(data['is_active'])

        if not fields_to_update:
            return internal_response(False, None, "No hay campos para actualizar")

        values.append(sucursal_id)
        query = f"""
            UPDATE sucursales
            SET {', '.join(fields_to_update)}, updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
            RETURNING id, restaurante_id, name, address, phone, email,
                      latitude, longitude, tolerance_minutes, is_active, created_at, updated_at
        """
        return DataBaseHandle.ExecuteNonQuery(query, tuple(values))

    def eliminar(self, sucursal_id: str) -> Dict[str, Any]:
        query = """
            DELETE FROM sucursales
            WHERE id = %s
        """
        return DataBaseHandle.ExecuteNonQuery(query, (sucursal_id,))
