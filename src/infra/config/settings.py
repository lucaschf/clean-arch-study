from pydantic_settings import BaseSettings

from .environment import Environment


class Settings(BaseSettings):
    """Singleton configuration class for application settings."""

    ENVIRONMENT: Environment = Environment.DEV
    """Specifies the current environment of the application."""

    TZ: str
    """Timezone to use for the application."""


__all__ = ["Settings"]
