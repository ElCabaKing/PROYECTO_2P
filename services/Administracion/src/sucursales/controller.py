from typing import Tuple, Dict, Any, Optional
from flask import request
from marshmallow import ValidationError
from src.shared.response import (
    response_success, response_inserted, response_updated,
    response_deleted, response_not_found, response_error, response_bad_request
)
from .dtos import CrearSucursalDTO, ActualizarSucursalDTO, SucursalResponseDTO
from .service import SucursalService


class SucursalController:

    def __init__(self):
        self.service = SucursalService()
        self.response_schema = SucursalResponseDTO()

    def obtener_todos(self, restaurante_id: Optional[str] = None) -> Tuple[Dict[str, Any], int]:
        result = self.service.obtener_todos(restaurante_id)
        if not result['result']:
            return response_error(result['message'])

        data = self.response_schema.dump(result['data'], many=True)
        return response_success(data)

    def obtener_por_id(self, sucursal_id: str) -> Tuple[Dict[str, Any], int]:
        result = self.service.obtener_por_id(sucursal_id)
        if not result['result']:
            if "no encontrada" in (result['message'] or "").lower():
                return response_not_found(result['message'])
            return response_error(result['message'])

        data = self.response_schema.dump(result['data'])
        return response_success(data)

    def crear(self) -> Tuple[Dict[str, Any], int]:
        try:
            schema = CrearSucursalDTO()
            data = schema.load(request.get_json())
        except ValidationError as err:
            return response_bad_request(str(err.messages))

        result = self.service.crear(data)
        if not result['result']:
            return response_error(result['message'])

        data = self.response_schema.dump(result['data'])
        return response_inserted(data)

    def actualizar(self, sucursal_id: str) -> Tuple[Dict[str, Any], int]:
        try:
            schema = ActualizarSucursalDTO()
            data = schema.load(request.get_json())
        except ValidationError as err:
            return response_bad_request(str(err.messages))

        result = self.service.actualizar(sucursal_id, data)
        if not result['result']:
            if "no encontrada" in (result['message'] or "").lower():
                return response_not_found(result['message'])
            return response_error(result['message'])

        data = self.response_schema.dump(result['data'])
        return response_updated(data)

    def eliminar(self, sucursal_id: str) -> Tuple[Dict[str, Any], int]:
        result = self.service.eliminar(sucursal_id)
        if not result['result']:
            if "no encontrada" in (result['message'] or "").lower():
                return response_not_found(result['message'])
            return response_error(result['message'])

        return response_deleted()
