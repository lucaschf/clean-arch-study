from fastapi import FastAPI

from src.infra.config import settings

from ...domain.__shared.error import DomainError
from ...domain.__shared.validator import ValidationError
from .exception_handlers import (
    domain_exception_handler,
    domain_validation_exception_handler,
    general_exception_handler,
)
from .middlewares import setup_cors, setup_sentry
from .routers import register_routes

app = FastAPI(
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
    title=settings.API_TITLE,
)

register_routes(app)
setup_sentry(app, settings.SENTRY_DSN)
setup_cors(app, settings.ALLOWED_ORIGINS)

app.add_exception_handler(ValidationError, domain_validation_exception_handler)
app.add_exception_handler(DomainError, domain_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

__all__ = ["app"]
