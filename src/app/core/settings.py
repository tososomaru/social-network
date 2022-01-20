from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    PROJECT_NAME: str = 'social-network'

    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8000

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    JWT_SECRET: str
    JWT_ALGORITHM: str = 'HS256'
    JWT_EXPIRATION: int = 3600

    FIRST_SUPERUSER_EMAIL: str
    FIRST_SUPERUSER_LOGIN: str
    FIRST_SUPERUSER_PASSWORD: str
    HEROKU_POSTGRESQL_IVORY_URL: str
    DATABASE_URL: str

    def get_db_url(self) -> str:
        if self.HEROKU_POSTGRESQL_IVORY_URL and self.HEROKU_POSTGRESQL_IVORY_URL.startswith("postgres://"):
            self.HEROKU_POSTGRESQL_IVORY_URL = self.HEROKU_POSTGRESQL_IVORY_URL.replace(
                "postgres://", "postgresql+asyncpg://", 1
            )

        return self.HEROKU_POSTGRESQL_IVORY_URL


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
