import os
from functools import lru_cache

from src.app.core.settings.app import AppSettings
from src.app.core.settings.dev import DevAppSettings
from src.app.core.settings.prod import ProdAppSettings

environment = {
    'dev': DevAppSettings,
    'prod': ProdAppSettings,
}


@lru_cache
def get_settings() -> AppSettings:
    settings = environment.get(os.environ.get('ENVIRONMENT_TYPE'))
    return settings()
