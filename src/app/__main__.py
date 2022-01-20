import uvicorn

from src.app.core.settings import settings

uvicorn.run(
    app='main:app',
    host=settings.SERVER_HOST,
    port=settings.SERVER_PORT,
    reload=True,
)
