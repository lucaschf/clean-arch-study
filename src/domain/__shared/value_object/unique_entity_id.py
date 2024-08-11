from dataclasses import dataclass, field
from typing import Iterable
from uuid import UUID, uuid4

from ..error import InvalidUUIDError
from .value_object import ValueObject


@dataclass(frozen=True, slots=True)
class UniqueEntityId(ValueObject):
    """A Value Object that represents a unique entity identifier.

    It is used to uniquely identify entities in the domain model.
    """
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        object.__setattr__(self, "id", str(self.id))
        self.__validate()

    def _get_equality_components(self) -> Iterable:
        return [self.id]

    def __validate(self) -> None:
        try:
            UUID(self.id)
        except ValueError as ex:
            raise InvalidUUIDError(uuid=self.id) from ex


__all__ = ["UniqueEntityId"]
