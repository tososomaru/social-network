import uvicorn

from src.app.core.settings import settings

uvicorn.run(
    app='src.app.app:app',
    host=settings.SERVER_HOST,
    port=settings.SERVER_PORT,
    reload=True,
)
