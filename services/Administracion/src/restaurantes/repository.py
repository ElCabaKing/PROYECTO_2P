from typing import Dict, Any
from src.core.database import DataBaseHandle
from src.shared.response import internal_response
from .repository_interface import IRestauranteRepository


class RestauranteRepository(IRestauranteRepository):

    def obtener_por_id(self, restaurante_id: str) -> Dict[str, Any]:
        """Get a restaurant by ID."""
        query = """
            SELECT id, name, legal_name, tax_id, logo_url, is_active, created_at, updated_at
            FROM restaurantes
            WHERE id = %s
        """
        return DataBaseHandle.getRecords(query, 1, (restaurante_id,))

    def obtener_todos(self) -> Dict[str, Any]:
        query = """
            SELECT id, name, legal_name, tax_id, logo_url, is_active, created_at, updated_at
            FROM restaurantes
            ORDER BY name
        """
        return DataBaseHandle.getRecords(query, 0)

    def crear(self, data: dict) -> Dict[str, Any]:
        query = """
            INSERT INTO restaurantes (name, legal_name, tax_id, logo_url)
            VALUES (%s, %s, %s, %s)
            RETURNING id, name, legal_name, tax_id, logo_url, is_active, created_at, updated_at
        """
        record = (
            data.get('name'),
            data.get('legal_name'),
            data.get('tax_id'),
            data.get('logo_url')
        )
        return DataBaseHandle.ExecuteNonQuery(query, record)

    def actualizar(self, restaurante_id: str, data: dict) -> Dict[str, Any]:
        # verificando el valor de los fields del req de la cabecera http
        fields_to_update = []
        values = []

        if 'name' in data and data['name'] is not None:
            fields_to_update.append("name = %s")
            values.append(data['name'])
        if 'legal_name' in data:
            fields_to_update.append("legal_name = %s")
            values.append(data['legal_name'])
        if 'tax_id' in data:
            fields_to_update.append("tax_id = %s")
            values.append(data['tax_id'])
        if 'logo_url' in data:
            fields_to_update.append("logo_url = %s")
            values.append(data['logo_url'])
        if 'is_active' in data and data['is_active'] is not None:
            fields_to_update.append("is_active = %s")
            values.append(data['is_active'])

        if not fields_to_update:
            return internal_response(False, None, "No hay campos para actualizar")

        values.append(restaurante_id)
        query = f"""
            UPDATE restaurantes
            SET {', '.join(fields_to_update)}, updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
            RETURNING id, name, legal_name, tax_id, logo_url, is_active, created_at, updated_at
        """
        return DataBaseHandle.ExecuteNonQuery(query, tuple(values))

    def eliminar(self, restaurante_id: str) -> Dict[str, Any]:
        """Delete a restaurant."""
        query = """
            DELETE FROM restaurantes
            WHERE id = %s
        """
        return DataBaseHandle.ExecuteNonQuery(query, (restaurante_id,))
