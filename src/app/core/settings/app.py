from pydantic import BaseSettings


class AppSettings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    PROJECT_NAME: str = 'social-network'

    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8000

    JWT_SECRET: str
    JWT_ALGORITHM: str = 'HS256'
    JWT_EXPIRATION: int = 3600

    FIRST_SUPERUSER_EMAIL: str
    FIRST_SUPERUSER_LOGIN: str
    FIRST_SUPERUSER_PASSWORD: str

    class Config:
        env_file = ".env"
