from src.app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):

    def get_db_url(self) -> str:
        return "sqlite:///./test.sqlite3"

    @property
    def database_kwargs(self):
        return dict()
