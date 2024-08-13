import contextlib
from collections import defaultdict

from .event import Event
from .event_dispatcher_interface import IEventDispatcher
from .event_handler_interface import IEventHandler


class EventDispatcher(IEventDispatcher):
    """A class that dispatches events to their handlers."""

    def __init__(self) -> None:
        """Initializes the event dispatcher."""
        self._handlers = defaultdict(list)

    def dispatch(self, event: Event) -> None:
        """Dispatches the event to the registered handlers."""
        handlers = self._handlers[event.name()]

        for handler in handlers:
            handler.handle(event)

    def register(self, event_name: str, event_handler: IEventHandler) -> None:
        """Registers a handler for a specific event name."""
        self._handlers[event_name].append(event_handler)

    def unregister(self, event_name: str, event_handler: IEventHandler) -> None:
        """Unregisters a handler for a specific event name."""
        with contextlib.suppress(ValueError):
            self._handlers[event_name].remove(event_handler)

    def unregister_all(self) -> None:
        """Unregisters all event handlers."""
        self._handlers.clear()


__all__ = ["EventDispatcher"]
