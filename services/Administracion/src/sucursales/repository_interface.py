from abc import ABC, abstractmethod
from typing import Dict, Any


class ISucursalRepository(ABC):
    """Interface for Sucursal repository operations."""

    @abstractmethod
    def obtener_por_id(self, sucursal_id: str) -> Dict[str, Any]:
        """Get branch by ID. Returns internal_response."""
        pass

    @abstractmethod
    def obtener_todos(self) -> Dict[str, Any]:
        """Get all branches. Returns internal_response."""
        pass

    @abstractmethod
    def obtener_por_restaurante(self, restaurante_id: str) -> Dict[str, Any]:
        """Get branches by restaurant ID. Returns internal_response."""
        pass

    @abstractmethod
    def crear(self, data: dict) -> Dict[str, Any]:
        """Create a new branch. Returns internal_response."""
        pass

    @abstractmethod
    def actualizar(self, sucursal_id: str, data: dict) -> Dict[str, Any]:
        """Update a branch. Returns internal_response."""
        pass

    @abstractmethod
    def eliminar(self, sucursal_id: str) -> Dict[str, Any]:
        """Delete a branch. Returns internal_response."""
        pass
