from abc import ABC, abstractmethod
from typing import List, Optional, Generic, TypeVar

T = TypeVar('T')
ID = TypeVar('ID')


class IRepository(ABC, Generic[T, ID]):
    @abstractmethod
    def get_by_id(self, entity_id: ID) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def create(self, entity: T) -> T:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self, entity_id: ID) -> bool:
        pass
