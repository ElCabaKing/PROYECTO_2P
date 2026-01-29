from typing import Tuple, Dict, Any
from flask import request
from marshmallow import ValidationError
from src.shared.response import (
    response_success, response_inserted, response_updated,
    response_deleted, response_not_found, response_error, response_bad_request
)
from .dtos import CrearPromocionDTO, ActualizarPromocionDTO, PromocionResponseDTO
from .service import PromocionService


class PromocionController:

    def __init__(self):
        self.service = PromocionService()
        self.response_schema = PromocionResponseDTO()

    def obtener_por_sucursal(self, sucursal_id: str) -> Tuple[Dict[str, Any], int]:
        result = self.service.obtener_por_sucursal(sucursal_id)
        if not result['result']:
            return response_error(result['message'])

        data = self.response_schema.dump(result['data'], many=True)
        return response_success(data)

    def obtener_activas(self, sucursal_id: str) -> Tuple[Dict[str, Any], int]:
        result = self.service.obtener_activas(sucursal_id)
        if not result['result']:
            return response_error(result['message'])

        data = self.response_schema.dump(result['data'], many=True)
        return response_success(data)

    def obtener_por_id(self, promocion_id: str) -> Tuple[Dict[str, Any], int]:
        result = self.service.obtener_por_id(promocion_id)
        if not result['result']:
            if "no encontrada" in (result['message'] or "").lower():
                return response_not_found(result['message'])
            return response_error(result['message'])

        data = self.response_schema.dump(result['data'])
        return response_success(data)

    def crear(self) -> Tuple[Dict[str, Any], int]:
        try:
            schema = CrearPromocionDTO()
            data = schema.load(request.get_json())
        except ValidationError as err:
            return response_bad_request(str(err.messages))

        result = self.service.crear(data)
        if not result['result']:
            return response_error(result['message'])

        data = self.response_schema.dump(result['data'])
        return response_inserted(data)

    def actualizar(self, promocion_id: str) -> Tuple[Dict[str, Any], int]:
        try:
            schema = ActualizarPromocionDTO()
            data = schema.load(request.get_json())
        except ValidationError as err:
            return response_bad_request(str(err.messages))

        result = self.service.actualizar(promocion_id, data)
        if not result['result']:
            if "no encontrada" in (result['message'] or "").lower():
                return response_not_found(result['message'])
            return response_error(result['message'])

        data = self.response_schema.dump(result['data'])
        return response_updated(data)

    def eliminar(self, promocion_id: str) -> Tuple[Dict[str, Any], int]:
        result = self.service.eliminar(promocion_id)
        if not result['result']:
            if "no encontrada" in (result['message'] or "").lower():
                return response_not_found(result['message'])
            return response_error(result['message'])

        return response_deleted()
