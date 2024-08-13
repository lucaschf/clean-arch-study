import json
from dataclasses import asdict, dataclass, field
from typing import Any, Optional


@dataclass(frozen=True, slots=True)
class ValidationErrorDetails:
    loc: tuple[str | int]
    msg: str
    input_value: Any
    context: Optional[dict[str, Any]] = field(default=None)

    def __str__(self) -> str:
        return json.dumps(asdict(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__str__()})"


__all__ = ["ValidationErrorDetails"]
