from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Optional

from ..validator.validator_interface import ValidationResult
from .external_entity_id import ExternalEntityId
from .unique_entity_id import UniqueEntityId


@dataclass(kw_only=True)
class AggregateRoot(ABC):
    """Base class for aggregate roots.

    Attributes:
        _id: The unique identifier for the aggregate root.
        _external_id: The external identifier for the aggregate root.
        created_at: The timestamp when the aggregate root was created.
        updated_at: The timestamp when the aggregate root was last updated.
    """
    _id: Optional[UniqueEntityId]
    _external_id: ExternalEntityId = field(default_factory=ExternalEntityId)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    @property
    def id(self) -> str:
        """Gets the string representation of the unique identifier.

        Returns:
            str: The string representation of the unique identifier.
        """
        return str(self._id)

    @property
    def external_id(self) -> str:
        """Gets the string representation of the external identifier.

        Returns:
            str: The string representation of the external identifier.
        """
        return str(self._external_id)

    @abstractmethod
    def validate(self) -> ValidationResult:
        """Validate the aggregate root.

        Raises:
            ValidationError: If the validation fails.
        """
        pass

    def __post_init__(self) -> None:
        """Post-initialization processing to validate the aggregate root."""
        validation_result = self.validate()
        if not validation_result.is_valid:
            raise validation_result.errors

    def to_dict(self) -> dict:
        """Converts the aggregate root to a dictionary.

        Returns:
            dict: A dictionary representation of the aggregate root.
        """
        entity_dict = asdict(self)

        entity_dict.pop('_id')
        entity_dict["id"] = self.id

        entity_dict.pop('_external_id')
        entity_dict["external_id"] = self.external_id

        return entity_dict


__all__ = ["AggregateRoot"]
