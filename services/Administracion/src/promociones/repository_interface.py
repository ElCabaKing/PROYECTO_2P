from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List


class IPromocionRepository(ABC):
    """Interface for Promocion repository operations."""

    @abstractmethod
    def obtener_por_id(self, promocion_id: str) -> Dict[str, Any]:
        """Get a promotion by ID."""
        pass

    @abstractmethod
    def obtener_por_sucursal(self, sucursal_id: str) -> Dict[str, Any]:
        """Get all promotions for a branch."""
        pass

    @abstractmethod
    def obtener_activas_por_sucursal(self, sucursal_id: str) -> Dict[str, Any]:
        """Get active promotions for a branch."""
        pass

    @abstractmethod
    def crear(self, data: dict) -> Dict[str, Any]:
        """Create a new promotion."""
        pass

    @abstractmethod
    def actualizar(self, promocion_id: str, data: dict) -> Dict[str, Any]:
        """Update a promotion."""
        pass

    @abstractmethod
    def eliminar(self, promocion_id: str) -> Dict[str, Any]:
        """Delete a promotion."""
        pass
