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
    POSTGRES_DATABASE_URL: str = "postgresql+asyncpg://postgres:admin@localhost:5432/social-network-db"

    def get_db_url(self) -> str:
        # return "sqlite:///test.db"
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@postgres:5432/{self.POSTGRES_DB}"


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
