import sentry_sdk
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from sentry_sdk.integrations.logging import LoggingIntegration


def setup_sentry(app: FastAPI, sentry_dsn: str | None) -> None:
    """Setup Sentry for error tracking."""
    if not sentry_dsn:
        return

    # Creates a new logging integration with event level and log level disabled
    # This is done to avoid log duplication in Sentry and the logging module
    sentry_logging = LoggingIntegration(
        level=None,  # Disables capturing breadcrumbs from logs
        event_level=None,  # Disables capturing events from logs
    )

    sentry_sdk.init(
        sentry_dsn,
        traces_sample_rate=1.0,
        integrations=[sentry_logging],
    )

    app.add_middleware(SentryAsgiMiddleware)


__all__ = ["setup_sentry"]
