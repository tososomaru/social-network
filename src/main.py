from fastapi import FastAPI

from src.app.api.api_v1.api import api_router
from src.app.api import docs
from src.app.core.config import get_settings
from src.app.api.api_v1.endpoints import users
from src.app.db.database import database


def get_application() -> FastAPI:
    settings = get_settings()
    application = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        debug=True
    )

    @application.on_event("startup")
    async def startup():
        await database.connect()

    @application.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

    application.include_router(docs.router, tags=['docs'])
    application.include_router(users.router, tags=['auth'])
    application.include_router(api_router, prefix=settings.API_V1_STR)

    return application


app = get_application()
