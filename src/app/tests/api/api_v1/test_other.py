import pytest
from starlette.testclient import TestClient


@pytest.mark.usefixtures("test_db_session")
def test_docs_redirect(client: TestClient):
    response = client.get("/")
    assert response.history[0].status_code == 307
    assert response.status_code == 200
    assert response.url == "http://testserver/docs"