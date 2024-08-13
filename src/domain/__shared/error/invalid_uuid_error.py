from dataclasses import dataclass

from .domain_error import DomainError


@dataclass(kw_only=True, frozen=True, slots=True)
class InvalidUUIDError(DomainError):
    """Exception raised for invalid UUIDs."""

    uuid: str
    message: str = "Invalid UUID"


__all__ = ["InvalidUUIDError"]
