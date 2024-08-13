from dataclasses import dataclass
from datetime import datetime

from src.domain.__shared.event import Event, EventDispatcher, IEventHandler


@dataclass(kw_only=True, frozen=True, slots=True)
class StubUserCreatedEvent(Event[dict]):
    """Represents a user creation event."""
    pass


@dataclass(kw_only=True, frozen=True, slots=True)
class StubOrderPlacedEvent(Event[dict]):
    """Represents an order placement event."""
    pass


class StubEventHandler(IEventHandler[Event]):
    def __init__(self) -> None:
        self.handled_events = []

    def handle(self, event: Event) -> None:  # noqa: D102
        self.handled_events.append(event)


def test_dispatch() -> None:
    dispatcher = EventDispatcher()
    handler = StubEventHandler()
    event = StubUserCreatedEvent(data={"user_id": "123"})
    dispatcher.register(event.name(), handler)
    dispatcher.dispatch(event)

    assert len(handler.handled_events) == 1
    assert handler.handled_events[0] == event


def test_register_and_unregister() -> None:
    dispatcher = EventDispatcher()
    handler1 = StubEventHandler()
    handler2 = StubEventHandler()
    event_name = "StubUserCreatedEvent"

    dispatcher.register(event_name, handler1)
    dispatcher.register(event_name, handler2)
    assert len(dispatcher._handlers[event_name]) == 2

    dispatcher.unregister(event_name, handler1)
    assert len(dispatcher._handlers[event_name]) == 1

    dispatcher.unregister_all()
    assert len(dispatcher._handlers) == 0


def test_unregister_nonexistent_handler() -> None:
    dispatcher = EventDispatcher()
    handler = StubEventHandler()

    dispatcher.unregister("test_event", handler)


def test_dispatch_no_handlers() -> None:
    dispatcher = EventDispatcher()
    event = Event(data="some data", timestamp=datetime.now())

    dispatcher.dispatch(event)
