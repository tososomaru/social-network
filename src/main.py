from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.app.api.api_v1.api import api_router
from src.app.api import docs
from src.app.core.settings import settings
from src.app.api.api_v1.endpoints import users
from src.app.db.base import get_database, database

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(docs.router, tags=['docs'])
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(users.router, tags=['auth'])

# Base.metadata.create_all(engine)

app

add_pagination(app)
