import uvicorn

from .settings import settings
from .database import migration_db


migration_db()

uvicorn.run(
    app='src.social_network.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
