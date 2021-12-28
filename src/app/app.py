import json

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi_pagination import add_pagination
from pydantic import ValidationError
from fastapi.responses import JSONResponse

from .api.api_v1.api import api_router
from .api import docs
from src.app.core.settings import settings
from .api.api_v1.endpoints import users
from .db.base import database, Base, engine

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    exc_json = json.loads(exc.json())

    r = {
        'messages': [error['msg'] for error in exc_json]
    }

    return JSONResponse(r, status_code=422)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(docs.router, tags=['docs'])
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(users.router, tags=['auth'])

Base.metadata.create_all(bind=engine)

add_pagination(app)
