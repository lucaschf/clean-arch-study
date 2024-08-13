from datetime import datetime

from src.domain.__shared.event import Event, IEventDispatcher, IEventHandler


class StubEventDispatcher(IEventDispatcher):
    def __init__(self) -> None:
        self.handlers = {}

    def dispatch(self, event: Event) -> None:  # noqa: D102
        event_name = event.__class__.__name__
        for handler in self.handlers.get(event_name, []):
            handler.handle(event)

    def register(self, event_name: str, event_handler: IEventHandler) -> None:  # noqa: D102
        self.handlers.setdefault(event_name, []).append(event_handler)

    def unregister(self, event_name: str, event_handler: IEventHandler) -> None:  # noqa: D102
        self.handlers.get(event_name, []).remove(event_handler)

    def unregister_all(self) -> None:  # noqa: D102
        self.handlers.clear()


class StubEventHandler(IEventHandler):
    def __init__(self) -> None:
        self.handled_events = []

    def handle(self, event: Event) -> None:  # noqa: D102
        self.handled_events.append(event)


# Pytest tests
def test_dispatch() -> None:
    dispatcher = StubEventDispatcher()
    handler = StubEventHandler()
    event = Event(data="some data", timestamp=datetime.now())

    dispatcher.register("Event", handler)
    dispatcher.dispatch(event)

    assert len(handler.handled_events) == 1
    assert handler.handled_events[0] == event


def test_register_and_unregister() -> None:
    dispatcher = StubEventDispatcher()
    handler1 = StubEventHandler()
    handler2 = StubEventHandler()

    dispatcher.register("Event", handler1)
    dispatcher.register("Event", handler2)
    assert len(dispatcher.handlers["Event"]) == 2

    dispatcher.unregister("Event", handler1)
    assert len(dispatcher.handlers["Event"]) == 1

    dispatcher.unregister_all()
    assert len(dispatcher.handlers) == 0
