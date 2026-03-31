from typing import Dict, Any, Optional
from src.shared.response import internal_response
from .repository import SucursalRepository


class SucursalService:
    """Service layer for Sucursal business logic."""

    def __init__(self):
        self.repository = SucursalRepository()

    def obtener_todos(self, restaurante_id: Optional[str] = None) -> Dict[str, Any]:
        """Get all branches, optionally filtered by restaurant."""
        if restaurante_id:
            result = self.repository.obtener_por_restaurante(restaurante_id)
        else:
            result = self.repository.obtener_todos()

        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, result['data'], None)

    def obtener_por_id(self, sucursal_id: str) -> Dict[str, Any]:
        """Get a branch by ID."""
        result = self.repository.obtener_por_id(sucursal_id)
        if not result['result']:
            return internal_response(False, None, result['message'])
        if not result['data']:
            return internal_response(False, None, "Sucursal no encontrada")
        return internal_response(True, result['data'], None)

    def crear(self, data: dict) -> Dict[str, Any]:
        """Create a new branch."""
        result = self.repository.crear(data)
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, result['data'], None)

    def actualizar(self, sucursal_id: str, data: dict) -> Dict[str, Any]:
        """Update a branch."""
        existing = self.repository.obtener_por_id(sucursal_id)
        if not existing['result'] or not existing['data']:
            return internal_response(False, None, "Sucursal no encontrada")

        result = self.repository.actualizar(sucursal_id, data)
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, result['data'], None)

    def eliminar(self, sucursal_id: str) -> Dict[str, Any]:
        """Delete a branch."""
        existing = self.repository.obtener_por_id(sucursal_id)
        if not existing['result'] or not existing['data']:
            return internal_response(False, None, "Sucursal no encontrada")

        result = self.repository.eliminar(sucursal_id)
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, None, "Sucursal eliminada")
