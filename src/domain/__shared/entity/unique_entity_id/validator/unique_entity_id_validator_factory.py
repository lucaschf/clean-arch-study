from src.domain.__shared.validator import IValidator

from .object_id_validator import ObjectIdValidator


class UniqueEntityIdValidatorFactory:
    """A factory class responsible for creating validators for UniqueEntityIds.

    This factory provides a centralized point for getting concrete validator
    implementations, adhering to the Dependency Inversion Principle. It currently
    returns an ObjectIdValidator, which is tailored for validating MongoDB ObjectIds.
    """

    @staticmethod
    def create() -> IValidator[str]:
        """Creates and returns a concrete validator for UniqueEntityIds.

        Returns:
            IValidator[str]:An instance of ObjectIdValidator for validating UniqueEntityIds.
        """
        return ObjectIdValidator()


__all__ = ["UniqueEntityIdValidatorFactory"]
