from abc import ABC, abstractmethod
from typing import Any, Dict, Iterable, Optional


class IRepository[T](ABC):
    """An abstract base class for repositories."""

    @abstractmethod
    def add(self, entity: T) -> T:
        """Adds an entity to the repository."""

    @abstractmethod
    def find(self, filters: Dict[str, Any]) -> Iterable[T]:
        """Returns all entities matching the given filter criteria."""

    @abstractmethod
    def find_one(self, filters: Dict[str, Any]) -> Optional[T]:
        """Returns the entity matching the given filter criteria if it exists."""

    def find_by_id(self, entity_id: str) -> Optional[T]:
        return self.find_one({"id": entity_id})

    def find_by_external_id(self, external_id: str) -> Optional[T]:
        """Returns the entity with the given external identifier if it exists."""
        return self.find_one({"external_id": external_id})


__all__ = ["IRepository"]
