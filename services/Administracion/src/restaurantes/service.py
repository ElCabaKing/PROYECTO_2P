from typing import Dict, Any
from src.shared.response import internal_response
from .repository import RestauranteRepository


class RestauranteService:

    def __init__(self):
        self.repository = RestauranteRepository()

    def obtener_todos(self) -> Dict[str, Any]:
        result = self.repository.obtener_todos()
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, result['data'], None)

    def obtener_por_id(self, restaurante_id: str) -> Dict[str, Any]:
        result = self.repository.obtener_por_id(restaurante_id)
        if not result['result']:
            return internal_response(False, None, result['message'])
        if not result['data']:
            return internal_response(False, None, "Restaurante no encontrado")
        return internal_response(True, result['data'], None)

    def crear(self, data: dict) -> Dict[str, Any]:
        result = self.repository.crear(data)
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, result['data'], None)

    def actualizar(self, restaurante_id: str, data: dict) -> Dict[str, Any]:
        # virificando si no existe
        existing = self.repository.obtener_por_id(restaurante_id)
        if not existing['result'] or not existing['data']:
            return internal_response(False, None, "Restaurante no encontrado")

        result = self.repository.actualizar(restaurante_id, data)
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, result['data'], None)

    def eliminar(self, restaurante_id: str) -> Dict[str, Any]:
        existing = self.repository.obtener_por_id(restaurante_id)
        if not existing['result'] or not existing['data']:
            return internal_response(False, None, "Restaurante no encontrado")

        result = self.repository.eliminar(restaurante_id)
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, None, "Restaurante eliminado")
