import json

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.responses import JSONResponse

from .api.api_v1.api import api_router
from .api import docs
from src.app.core.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    print(f"OMG! The client sent invalid data!: {exc}")
    exc_json = json.loads(exc.json())
    response = {"message": [], "data": None}

    for error in exc_json:
        response['message'].append(error['loc'][-1]+f": {error['msg']}")

    return JSONResponse(response, status_code=422)

app.include_router(docs.router, tags=['docs'])
app.include_router(api_router, prefix=settings.API_V1_STR)
