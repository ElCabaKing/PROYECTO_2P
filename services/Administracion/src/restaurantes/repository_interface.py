from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any


class IRestauranteRepository(ABC):
    """Interface for Restaurante repository operations."""

    @abstractmethod
    def obtener_por_id(self, restaurante_id: str) -> Dict[str, Any]:
        """Get restaurant by ID. Returns internal_response."""
        pass

    @abstractmethod
    def obtener_todos(self) -> Dict[str, Any]:
        """Get all restaurants. Returns internal_response."""
        pass

    @abstractmethod
    def crear(self, data: dict) -> Dict[str, Any]:
        """Create a new restaurant. Returns internal_response."""
        pass

    @abstractmethod
    def actualizar(self, restaurante_id: str, data: dict) -> Dict[str, Any]:
        """Update a restaurant. Returns internal_response."""
        pass

    @abstractmethod
    def eliminar(self, restaurante_id: str) -> Dict[str, Any]:
        """Delete a restaurant. Returns internal_response."""
        pass
