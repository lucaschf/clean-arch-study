"""Domain Event Management.

This package provides essential building blocks for implementing a domain event-driven system
 within a DDD architecture.

Key elements:

* `Event`:
    An abstract base class representing domain events, encapsulating data and timestamp information
    crucial for decoupling domain logic from external concerns.
* `EventDispatcher`:
    A concrete implementation of the `IEventDispatcher` interface, responsible for orchestrating
     the communication between domain events and their handlers.
* `IEventDispatcher`: An interface defining the contract for event dispatchers,
    promoting loose coupling and adaptability to different implementations.
* `IEventHandler`: An interface defining the contract for event handlers,
    ensuring consistent handling logic across various domain events.
"""

from .event import Event
from .event_dispatcher import EventDispatcher
from .event_dispatcher_interface import IEventDispatcher
from .event_handler_interface import IEventHandler

__all__ = [
    "Event",
    "EventDispatcher",
    "IEventDispatcher",
    "IEventHandler",
]
