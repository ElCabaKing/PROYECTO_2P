from typing import Dict, Any, Optional
from src.shared.response import internal_response
from .repository import MesaRepository


class MesaService:

    def __init__(self):
        self.repository = MesaRepository()

    def obtener_todos(self, sucursal_id: Optional[str] = None) -> Dict[str, Any]:
        if sucursal_id:
            result = self.repository.obtener_por_sucursal(sucursal_id)
        else:
            result = self.repository.obtener_todos()

        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, result['data'], None)

    def obtener_por_id(self, mesa_id: str) -> Dict[str, Any]:
        result = self.repository.obtener_por_id(mesa_id)
        if not result['result']:
            return internal_response(False, None, result['message'])
        if not result['data']:
            return internal_response(False, None, "Mesa no encontrada")
        return internal_response(True, result['data'], None)

    def obtener_disponibles_por_capacidad(self, sucursal_id: str, num_personas: int) -> Dict[str, Any]:
        result = self.repository.obtener_disponibles_por_capacidad(sucursal_id, num_personas)
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, result['data'], None)

    def crear(self, data: dict) -> Dict[str, Any]:
        # validando la capacidad de espacios en la mesa
        capacity_min = data.get('capacity_min', 1)
        capacity_max = data.get('capacity_max')
        if capacity_min > capacity_max:
            return internal_response(False, None, "capacity_min no puede ser mayor que capacity_max")

        
        next_num_result = self.repository.obtener_siguiente_numero_mesa(str(data.get('sucursal_id')))
        if not next_num_result['result']:
            return internal_response(False, None, next_num_result['message'])

        data['table_number'] = str(next_num_result['data']['next_number'])

        result = self.repository.crear(data)
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, result['data'], None)

    def actualizar(self, mesa_id: str, data: dict) -> Dict[str, Any]:
        existing = self.repository.obtener_por_id(mesa_id)
        if not existing['result'] or not existing['data']:
            return internal_response(False, None, "Mesa no encontrada")

        # validando la capacidad ya existente
        current = existing['data']
        new_min = data.get('capacity_min', current['capacity_min'])
        new_max = data.get('capacity_max', current['capacity_max'])
        if new_min > new_max:
            return internal_response(False, None, "capacity_min no puede ser mayor que capacity_max")

        result = self.repository.actualizar(mesa_id, data)
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, result['data'], None)

    def eliminar(self, mesa_id: str) -> Dict[str, Any]:
        existing = self.repository.obtener_por_id(mesa_id)
        if not existing['result'] or not existing['data']:
            return internal_response(False, None, "Mesa no encontrada")

        result = self.repository.eliminar(mesa_id)
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, None, "Mesa eliminada")
