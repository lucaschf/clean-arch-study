from abc import ABC, abstractmethod

from .event import Event
from .event_handler_interface import IEventHandler


class IEventDispatcher(ABC):
    """Abstract base for domain event dispatchers.

    Orchestrates event-handler communication.
    """

    @abstractmethod
    def dispatch(self, event: Event) -> None:
        """Dispatches an event to registered handlers."""

    @abstractmethod
    def register(self, event_name: str, event_handler: IEventHandler) -> None:
        """Registers a handler for a specific event name."""

    @abstractmethod
    def unregister(self, event_name: str, event_handler: IEventHandler) -> None:
        """Unregisters a handler for a specific event name."""

    @abstractmethod
    def unregister_all(self) -> None:
        """Unregisters all event handlers."""


__all__ = ["IEventDispatcher"]
