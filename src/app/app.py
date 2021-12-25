from fastapi import FastAPI

from .api.api_v1.api import api_router
from .api import docs
from src.app.core.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(docs.router, tags=['docs'])
app.include_router(api_router, prefix=settings.API_V1_STR)
