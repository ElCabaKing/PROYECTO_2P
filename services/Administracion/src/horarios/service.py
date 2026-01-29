from typing import Dict, Any
from src.shared.response import internal_response
from .repository import HorarioRepository


class HorarioService:

    def __init__(self):
        self.repository = HorarioRepository()

    def obtener_por_sucursal(self, sucursal_id: str) -> Dict[str, Any]:
        result = self.repository.obtener_por_sucursal(sucursal_id)
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, result['data'], None)

    def obtener_por_id(self, horario_id: str) -> Dict[str, Any]:
        result = self.repository.obtener_por_id(horario_id)
        if not result['result']:
            return internal_response(False, None, result['message'])
        if not result['data']:
            return internal_response(False, None, "Horario no encontrado")
        return internal_response(True, result['data'], None)

    def crear(self, data: dict) -> Dict[str, Any]:
        # verificando si ya existe un horario en la sucursal
        sucursal_id = str(data.get('sucursal_id'))
        day_of_week = data.get('day_of_week')

        existing = self.repository.obtener_por_sucursal_y_dia(sucursal_id, day_of_week)
        if existing['result'] and existing['data']:
            return internal_response(False, None, "Ya existe un horario para este día")

        result = self.repository.crear(data)
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, result['data'], None)

    def actualizar(self, horario_id: str, data: dict) -> Dict[str, Any]:
        existing = self.repository.obtener_por_id(horario_id)
        if not existing['result'] or not existing['data']:
            return internal_response(False, None, "Horario no encontrado")

        # cambiando por un dia de la semana
        if 'day_of_week' in data and data['day_of_week'] is not None:
            current = existing['data']
            conflict = self.repository.obtener_por_sucursal_y_dia(
                str(current['sucursal_id']),
                data['day_of_week']
            )
            if conflict['result'] and conflict['data'] and str(conflict['data']['id']) != horario_id:
                return internal_response(False, None, "Ya existe un horario para este día")

        result = self.repository.actualizar(horario_id, data)
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, result['data'], None)

    def eliminar(self, horario_id: str) -> Dict[str, Any]:
        existing = self.repository.obtener_por_id(horario_id)
        if not existing['result'] or not existing['data']:
            return internal_response(False, None, "Horario no encontrado")

        result = self.repository.eliminar(horario_id)
        if not result['result']:
            return internal_response(False, None, result['message'])
        return internal_response(True, None, "Horario eliminado")
