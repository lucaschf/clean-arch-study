from dataclasses import FrozenInstanceError
from datetime import datetime
from unittest.mock import patch

import pytest

from src.domain.__shared.entity import AggregateRoot, ExternalEntityId
from src.domain.__shared.validator import ValidationError, ValidationErrorDetails, ValidationResult


class StubEntity(AggregateRoot):
    def validate(self) -> ValidationResult:  # noqa: D102
        return ValidationResult(is_valid=True)


def test_aggregate_root_creation() -> None:
    aggregate_root = StubEntity(_external_id=ExternalEntityId())
    assert isinstance(aggregate_root.id, str)
    assert isinstance(aggregate_root.external_id, str)
    assert isinstance(aggregate_root.created_at, datetime)
    assert isinstance(aggregate_root.updated_at, datetime)


def test_aggregate_root_to_dict() -> None:
    aggregate_root = StubEntity(_external_id=ExternalEntityId())
    aggregate_dict = aggregate_root.to_dict()
    assert "id" in aggregate_dict
    assert "external_id" in aggregate_dict
    assert "created_at" in aggregate_dict
    assert "updated_at" in aggregate_dict
    assert "_id" not in aggregate_dict
    assert "_external_id" not in aggregate_dict


def test_aggregate_root_validation_success() -> None:
    aggregate_root = StubEntity(_external_id=ExternalEntityId())
    aggregate_root.__post_init__()


def test_aggregate_root_validation_failure() -> None:
    class InvalidAggregateRoot(AggregateRoot):
        def validate(self) -> ValidationResult:
            return ValidationResult(
                is_valid=False,
                errors=(
                    ValidationErrorDetails(
                        msg="Validation error",
                        loc=("field",),
                        input_value="invalid",
                    ),
                ),
            )

    with pytest.raises(ValidationError):
        InvalidAggregateRoot()


def test_aggregate_root_immutability() -> None:
    aggregate_root = StubEntity(_external_id=ExternalEntityId())
    with pytest.raises(FrozenInstanceError):
        # noinspection PyDataclass
        aggregate_root._id = "new_id"

    with pytest.raises(FrozenInstanceError):
        # noinspection PyDataclass
        aggregate_root._external_id = "new_external_id"


def test_aggregate_root_calls_validate() -> None:
    with patch.object(StubEntity, "validate") as mock_validate:
        mock_validate.return_value = ValidationResult(is_valid=True)
        StubEntity()

    mock_validate.assert_called_once()
