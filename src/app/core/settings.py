from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    PROJECT_NAME: str = 'social-network'

    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8000

    SQLITE3_URL: str = 'sqlite:///./database.sqlite3'

    JWT_SECRET: str
    JWT_ALGORITHM: str = 'HS256'
    JWT_EXPIRATION: int = 3600

    FIRST_SUPERUSER_EMAIL: str
    FIRST_SUPERUSER_LOGIN: str
    FIRST_SUPERUSER_PASSWORD: str


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
