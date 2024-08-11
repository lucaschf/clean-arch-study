class DomainError(Exception):
    """A custom exception class used to handle domain-specific exceptions."""

    def __init__(self, message: str | None, inner_error: Exception | None = None) -> None:
        """Constructs a new DomainException.

        Args:
            message: The exception message.
            inner_error: An optional inner exception that caused this exception.
        """
        super().__init__(message)
        self._message: str | None = message
        self._inner_error: Exception | None = inner_error

    @property
    def inner_error(self) -> Exception | None:
        """Returns the inner exception that caused this exception.

        Returns:
            Exception: The inner exception that caused this exception.
        """
        return self._inner_error

    @property
    def message(self) -> str | None:
        """Returns the exception message.

        Returns:
            str: The exception message.
        """
        return self._message


__all__ = ["DomainError"]
