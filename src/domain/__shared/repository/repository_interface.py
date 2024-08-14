from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.__shared.entity import UniqueEntityId


class IRepository[T](ABC):
    """Interface for a generic repository.

    This interface defines the basic CRUD operations for a repository.
    """

    @abstractmethod
    def create(self, entity: T) -> T:
        """Create a new entity in the repository.

        Args:
            entity (T): The entity to be created.

        Returns:
            T: The created entity.
        """
        pass

    @abstractmethod
    def find_by_id(self, identifier: str | UniqueEntityId) -> Optional[T]:
        """Find an entity by its identifier.

        Args:
            identifier (str | UniqueEntityId): The identifier of the entity.

        Returns:
            Optional[T]: The found entity or None if not found.
        """
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        """Find all entities in the repository.

        Returns:
            List[T]: A list of all entities.
        """
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        """Update an existing entity in the repository.

        Args:
            entity (T): The entity to be updated.

        Returns:
            T: The updated entity.
        """
        pass


__all__ = ["IRepository"]
