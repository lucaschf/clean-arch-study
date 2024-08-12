from dataclasses import dataclass, field
from uuid import UUID, uuid4

from ..error import InvalidUUIDError
from ..value_object import ValueObject


@dataclass(frozen=True, slots=True)
class ExternalEntityId(ValueObject):
    """Represents an external entity identifier.

    Attributes:
        id (str): The unique identifier for the external entity, defaulting to a new UUID.
    """
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        """Performs post-initialization validation and normalization of the `id` attribute."""
        object.__setattr__(self, "id", str(self.id) if self.id else None)
        self.__validate()

    def __validate(self) -> None:
        """Validates the UUID format of the id.

        Raises:
            InvalidUUIDError: If the id is not a valid UUID.
        """
        try:
            UUID(self.id)
        except (ValueError, TypeError) as ex:
            raise InvalidUUIDError(uuid=self.id) from ex


__all__ = ["ExternalEntityId"]
