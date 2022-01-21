from src.app.core.settings.base import AppSettings


class ProdAppSettings(AppSettings):
    HEROKU_POSTGRESQL_IVORY_URL: str

    def get_db_url(self) -> str:
        if self.HEROKU_POSTGRESQL_IVORY_URL and self.HEROKU_POSTGRESQL_IVORY_URL.startswith("postgres://"):
            self.HEROKU_POSTGRESQL_IVORY_URL = self.HEROKU_POSTGRESQL_IVORY_URL.replace(
                "postgres://", "postgresql+asyncpg://", 1
            )

        return self.HEROKU_POSTGRESQL_IVORY_URL
