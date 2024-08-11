from abc import ABC, abstractmethod


class IValidator[T](ABC):

    @abstractmethod
    def validate(self, value: T) -> None:
        pass


__all__ = ["IValidator"]
