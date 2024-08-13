from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True, slots=True)
class PagedResult[T]:
    items: Iterable[T]
    size: int
    page: int
    total: int
    pages: int


__all__ = ["PagedResult"]
