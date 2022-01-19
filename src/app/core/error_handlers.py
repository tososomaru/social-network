import json

from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.responses import JSONResponse

from app.main import app


@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    exc_json = json.loads(exc.json())

    r = {
        'messages': [error['msg'] for error in exc_json]
    }

    return JSONResponse(r, status_code=422)