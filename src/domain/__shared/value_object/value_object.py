import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, fields


@dataclass(frozen=True, slots=True)
class ValueObject(ABC):
    """An abstract base class for Value Objects.

    Value Objects are immutable objects that are defined by their values,
    not their identity.

    They are typically used to represent domain concepts.
    """

    @abstractmethod
    def _validate(self) -> None:
        """Validate the value object.

        Raises:
            DomainError: If the value object is invalid.
        """

    def __post_init__(self) -> None:
        """Validate the value object after initialization."""
        self._validate()

    def __str__(self) -> str:
        field_names = [f.name for f in fields(self)]
        if len(field_names) > 1:
            return json.dumps({
                field_name: getattr(self, field_name)
                for field_name in field_names
            })

        return str(getattr(self, field_names[0]))


__all__ = ["ValueObject"]
