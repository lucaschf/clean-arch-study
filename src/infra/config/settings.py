from pydantic import HttpUrl
from pydantic_settings import BaseSettings

from .environment import Environment


class Settings(BaseSettings):
    """Singleton configuration class for application settings."""

    ENVIRONMENT: Environment = Environment.DEV
    """Specifies the current environment of the application."""

    TZ: str = "America/Sao_Paulo"
    """Timezone to use for the application."""

    DOCS_URL: str = "/docs"
    """The URL for the swagger documentation."""

    REDOC_URL: str = "/redoc"
    """The URL for the redoc documentation."""

    API_TITLE: str = "Boilerplate"
    """The title for the API documentation."""

    SENTRY_DSN: HttpUrl | None = None
    """The DSN for Sentry error tracking."""

    ALLOWED_ORIGINS: list[str]
    """The allowed origins for CORS."""


__all__ = ["Settings"]
