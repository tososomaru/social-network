from pydantic import BaseSettings




settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
