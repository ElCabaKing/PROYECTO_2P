from abc import ABC, abstractmethod
from typing import Dict, Any


class IHorarioRepository(ABC):
    """Interface for Horario repository operations."""

    @abstractmethod
    def obtener_por_id(self, horario_id: str) -> Dict[str, Any]:
        """Get schedule by ID. Returns internal_response."""
        pass

    @abstractmethod
    def obtener_por_sucursal(self, sucursal_id: str) -> Dict[str, Any]:
        """Get schedules by branch ID. Returns internal_response."""
        pass

    @abstractmethod
    def obtener_por_sucursal_y_dia(self, sucursal_id: str, day_of_week: int) -> Dict[str, Any]:
        """Get schedule by branch and day. Returns internal_response."""
        pass

    @abstractmethod
    def crear(self, data: dict) -> Dict[str, Any]:
        """Create a new schedule. Returns internal_response."""
        pass

    @abstractmethod
    def actualizar(self, horario_id: str, data: dict) -> Dict[str, Any]:
        """Update a schedule. Returns internal_response."""
        pass

    @abstractmethod
    def eliminar(self, horario_id: str) -> Dict[str, Any]:
        """Delete a schedule. Returns internal_response."""
        pass
