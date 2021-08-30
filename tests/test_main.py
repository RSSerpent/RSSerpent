from starlette.testclient import TestClient

from rsserpent.main import app


def test_index() -> None:
    """Test if the index route works properly."""
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "RSSerpent is up & running" in response.text
