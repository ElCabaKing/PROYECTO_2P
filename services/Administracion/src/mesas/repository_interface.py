from abc import ABC, abstractmethod
from typing import Dict, Any


class IMesaRepository(ABC):
    """Interface for Mesa repository operations."""

    @abstractmethod
    def obtener_por_id(self, mesa_id: str) -> Dict[str, Any]:
        """Get table by ID. Returns internal_response."""
        pass

    @abstractmethod
    def obtener_todos(self) -> Dict[str, Any]:
        """Get all tables. Returns internal_response."""
        pass

    @abstractmethod
    def obtener_por_sucursal(self, sucursal_id: str) -> Dict[str, Any]:
        """Get tables by branch ID. Returns internal_response."""
        pass

    @abstractmethod
    def obtener_disponibles_por_capacidad(self, sucursal_id: str, num_personas: int) -> Dict[str, Any]:
        """Get available tables by capacity. Returns internal_response."""
        pass

    @abstractmethod
    def crear(self, data: dict) -> Dict[str, Any]:
        """Create a new table. Returns internal_response."""
        pass

    @abstractmethod
    def actualizar(self, mesa_id: str, data: dict) -> Dict[str, Any]:
        """Update a table. Returns internal_response."""
        pass

    @abstractmethod
    def eliminar(self, mesa_id: str) -> Dict[str, Any]:
        """Delete a table. Returns internal_response."""
        pass
