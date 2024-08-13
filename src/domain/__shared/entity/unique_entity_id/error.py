from dataclasses import dataclass

from src.domain.__shared.error import DomainError


@dataclass(kw_only=True, frozen=True, slots=True)
class InvalidEntityUniqueIdError(DomainError):
    """Exception raised for invalid Object Ids."""

    message: str = "Invalid entity Id"
    entity_id: str


__all__ = ["InvalidEntityUniqueIdError"]
