from .domain_error import DomainError


class InvalidUUIDError(DomainError):
    """Exception raised for invalid UUIDs."""

    def __init__(self, uuid: str, message: str = "Invalid UUID") -> None:
        super().__init__(message)
        self.uuid = uuid


__all__ = ["InvalidUUIDError"]
