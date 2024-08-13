from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Event[T](ABC):
    """A class representing a domain event.

    It encapsulates data associated with a significant
    occurrence within the domain and the timestamp when it happened.

    Attributes:
        data: The data payload of the event, representing the specifics of what occurred.
        timestamp: The datetime when the event took place.
    """
    data: T
    timestamp: datetime = field(default_factory=datetime.now)

    @classmethod
    def name(cls) -> str:
        """Returns the name of the event."""
        return cls.__name__


__all__ = ["Event"]
