from fastapi import FastAPI

from src.app.api import docs
from src.app.api.api_v1.api import api_router
from src.app.core.settings import settings
from src.app.db.init_db import init_db
from src.app.db.session import Session


def init() -> None:
    db = Session()
    init_db(db)


init()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(docs.router, tags=['docs'])
app.include_router(api_router, prefix=settings.API_V1_STR)
