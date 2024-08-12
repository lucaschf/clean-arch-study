from dataclasses import dataclass, field

from ...value_object import ValueObject
from .validator import UniqueEntityIdValidatorFactory


@dataclass(frozen=True, slots=True)
class UniqueEntityId(ValueObject):
    """A Value Object that represents a unique entity identifier.

    It is used to uniquely identify entities in the domain model.
    """
    id: str = field()

    def __post_init__(self) -> None:
        self.__validate()

    def __validate(self) -> None:
        UniqueEntityIdValidatorFactory.create().validate_or_raise(self.id)


__all__ = ["UniqueEntityId"]
