from .cors_middleware import setup_cors
from .sentry_middleware import setup_sentry

__all__ = ["setup_cors", "setup_sentry"]
