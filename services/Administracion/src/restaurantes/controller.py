from typing import Tuple, Dict, Any
from flask import request
from marshmallow import ValidationError
from src.shared.response import (
    response_success, response_inserted, response_updated,
    response_deleted, response_not_found, response_error, response_bad_request
)
from .dtos import CrearRestauranteDTO, RestauranteResponseDTO, ActualizarRestauranteDTO
from .service import RestauranteService


class RestauranteController:


    def __init__(self):
        self.service = RestauranteService()
        self.response_schema = RestauranteResponseDTO()

    def obtener_todos(self) -> Tuple[Dict[str, Any], int]:
        result = self.service.obtener_todos()
        if not result['result']:
            return response_error(result['message'])

        # Serialize response
        data = self.response_schema.dump(result['data'], many=True)
        return response_success(data)

    def obtener_por_id(self, restaurante_id: str) -> Tuple[Dict[str, Any], int]:
        result = self.service.obtener_por_id(restaurante_id)
        if not result['result']:
            if "no encontrado" in (result['message'] or "").lower():
                return response_not_found(result['message'])
            return response_error(result['message'])

        data = self.response_schema.dump(result['data'])
        return response_success(data)

    def crear(self) -> Tuple[Dict[str, Any], int]:
        try:
            schema = CrearRestauranteDTO()
            data = schema.load(request.get_json())
        except ValidationError as err:
            return response_bad_request(str(err.messages))

        result = self.service.crear(data)
        if not result['result']:
            return response_error(result['message'])

        data = self.response_schema.dump(result['data'])
        return response_inserted(data)

    def actualizar(self, restaurante_id: str) -> Tuple[Dict[str, Any], int]:
        try:
            schema = ActualizarRestauranteDTO()
            data = schema.load(request.get_json())
        except ValidationError as err:
            return response_bad_request(str(err.messages))

        result = self.service.actualizar(restaurante_id, data)
        if not result['result']:
            if "no encontrado" in (result['message'] or "").lower():
                return response_not_found(result['message'])
            return response_error(result['message'])

        data = self.response_schema.dump(result['data'])
        return response_updated(data)

    def eliminar(self, restaurante_id: str) -> Tuple[Dict[str, Any], int]:
        result = self.service.eliminar(restaurante_id)
        if not result['result']:
            if "no encontrado" in (result['message'] or "").lower():
                return response_not_found(result['message'])
            return response_error(result['message'])

        return response_deleted()
