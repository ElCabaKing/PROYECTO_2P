from typing import Dict, Any
from src.shared.response import internal_response
from .repository import PromocionRepository


class PromocionService:

    def __init__(self):
        self.repository = PromocionRepository()

    def obtener_por_sucursal(self, sucursal_id: str) -> Dict[str, Any]:
        result = self.repository.obtener_por_sucursal(sucursal_id)
        if not result['result']:
            return internal_response(False, None, result.get('error', 'Error al obtener promociones'))
        return internal_response(True, result['data'], None)

    def obtener_activas(self, sucursal_id: str) -> Dict[str, Any]:
        result = self.repository.obtener_activas_por_sucursal(sucursal_id)
        if not result['result']:
            return internal_response(False, None, result.get('error', 'Error al obtener promociones activas'))
        return internal_response(True, result['data'], None)

    def obtener_por_id(self, promocion_id: str) -> Dict[str, Any]:
        result = self.repository.obtener_por_id(promocion_id)
        if not result['result']:
            return internal_response(False, None, result.get('error', 'Error al obtener promoción'))
        if not result['data']:
            return internal_response(False, None, "Promoción no encontrada")
        return internal_response(True, result['data'], None)

    def crear(self, data: dict) -> Dict[str, Any]:
        result = self.repository.crear(data)
        if not result['result']:
            return internal_response(False, None, result.get('error', 'Error al crear promoción'))
        return internal_response(True, result['data'], None)

    def actualizar(self, promocion_id: str, data: dict) -> Dict[str, Any]:
        existing = self.repository.obtener_por_id(promocion_id)
        if not existing['result'] or not existing['data']:
            return internal_response(False, None, "Promoción no encontrada")

        result = self.repository.actualizar(promocion_id, data)
        if not result['result']:
            return internal_response(False, None, result.get('error', 'Error al actualizar promoción'))
        return internal_response(True, result['data'], None)

    def eliminar(self, promocion_id: str) -> Dict[str, Any]:
        existing = self.repository.obtener_por_id(promocion_id)
        if not existing['result'] or not existing['data']:
            return internal_response(False, None, "Promoción no encontrada")

        result = self.repository.eliminar(promocion_id)
        if not result['result']:
            return internal_response(False, None, result.get('error', 'Error al eliminar promoción'))
        return internal_response(True, True, None)
