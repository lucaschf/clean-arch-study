from src.domain.__shared.error import DomainError


class InvalidEntityUniqueIdError(DomainError):
    """Exception raised for invalid Object Ids."""

    def __init__(self, entity_id: str, message: str = "Invalid entity Id") -> None:
        super().__init__(message)
        self.entity_id = entity_id


__all__ = ["InvalidEntityUniqueIdError"]
