from typing import Dict

from fastapi import Depends
from requests import Response
from starlette.testclient import TestClient

from src.app.core.config import get_settings
from src.app.core.settings.app import AppSettings


def register(
        client: TestClient,
        settings: AppSettings = Depends(get_settings)
) -> Response:
    data = {
        'email': settings.FIRST_SUPERUSER_EMAIL,
        'username': settings.FIRST_SUPERUSER_LOGIN,
        'password': settings.FIRST_SUPERUSER_PASSWORD,
        'password_confirm': settings.FIRST_SUPERUSER_PASSWORD,
        'is_superuser': True
    }
    r = client.post(
        f"{settings.API_V1_STR}/auth/register/",
        json=data,
    )
    return r


def login(
        client: TestClient,
        settings: AppSettings = Depends(get_settings)
) -> Response:
    login_data = {
        "username": settings.FIRST_SUPERUSER_LOGIN,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/auth/login/", data=login_data)
    return r


def get_superuser_token_headers(client: TestClient) -> Dict[str, str]:
    r = login(client)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers
