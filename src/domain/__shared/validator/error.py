from typing import Iterable

from src.domain.__shared.error import DomainError
from src.domain.__shared.validator.error_details import ValidationErrorDetails


class ValidationError(DomainError):
    """A class representing a validation error."""

    def __init__(self, errors: Iterable[ValidationErrorDetails]) -> None:
        super().__init__("Validation error")
        self.errors = errors or []

    def __str__(self) -> str:
        errors_count = len(self.errors)
        errors_as_str = ', '.join([str(error) for error in self.errors])
        return (f"{errors_count} Validation error{'s' if errors_count > 1 else ''}:"
                f" {errors_as_str}")


__all__ = ["ValidationError"]
