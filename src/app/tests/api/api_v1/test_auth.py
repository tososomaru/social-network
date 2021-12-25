import pytest
from starlette.testclient import TestClient

from src.app.core.settings import settings
from ..utils import login, register, get_superuser_token_headers


class TestAuthEndpoint:
    @pytest.mark.usefixtures("test_db_session")
    def test_register(self, client: TestClient):
        r = register(client)
        assert r.status_code == 200

    @pytest.mark.usefixtures("test_db_session")
    def test_login(self, client: TestClient):
        register(client)
        r = login(client)

        assert r.status_code == 200

    @pytest.mark.usefixtures("test_db_session")
    def test_me(self, client: TestClient):
        register(client)
        login(client)
        response = client.get(
            f"{settings.API_V1_STR}/auth/me/",
            headers=get_superuser_token_headers(client)
        )

        assert response.status_code == 200

