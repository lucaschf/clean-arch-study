from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from datetime import datetime

from src.domain.__shared.value_object import UniqueEntityId


@dataclass(kw_only=True)
class AggregateRoot(ABC):
    """Base class for aggregate roots."""
    _id: UniqueEntityId = field(default_factory=UniqueEntityId)

    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    @property
    def id(self) -> str:
        return str(self._id)

    @abstractmethod
    def validate(self) -> None:
        """Validate the aggregate root.

        Raises:s
           DomainError: If the validation fails.
        """
        pass

    def __post_init__(self) -> None:
        self.validate()

    def to_dict(self) -> dict:
        entity_dict = asdict(self)
        entity_dict.pop('_id')
        entity_dict["id"] = self.id

        return entity_dict


__all__ = ["AggregateRoot"]
