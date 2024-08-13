from typing import Any

from bson import ObjectId

from src.domain.__shared.validator import IValidator, ValidationErrorDetails, ValidationResult


class ObjectIdValidator(IValidator[str]):
    def validate(self, value: Any) -> ValidationResult:  # noqa: ANN401
        if not isinstance(value, str):
            return ValidationResult(
                is_valid=False,
                errors=(
                    ValidationErrorDetails(
                        loc=("id",),
                        msg="Invalid Object Id",
                        input_value=str(value),
                        context={"expected_type": "str", "received_type": type(value).__name__},
                    ),
                ),
            )

        if not ObjectId.is_valid(value):
            return ValidationResult(
                is_valid=False,
                errors=(
                    ValidationErrorDetails(loc=("id",), msg="Invalid Object Id", input_value=value),
                ),
            )

        return ValidationResult(is_valid=True)


__all__ = ["ObjectIdValidator"]
