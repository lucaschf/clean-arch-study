from abc import ABC, abstractmethod

from .event import Event


class IEventHandler[T: Event](ABC):
    """An abstract base class for event handlers."""

    @abstractmethod
    def handle(self, event: T) -> None:
        """Handles the given event."""


__all__ = ["IEventHandler"]
