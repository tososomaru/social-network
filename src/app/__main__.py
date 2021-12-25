import uvicorn

from src.app.core.settings import settings
from src.app.db.init_db import init_db
from src.app.db.session import Session


def init() -> None:
    db = Session()
    init_db(db)


init()

uvicorn.run(
    app='src.app.app:app',
    host=settings.SERVER_HOST,
    port=settings.SERVER_PORT,
    reload=True,
)
