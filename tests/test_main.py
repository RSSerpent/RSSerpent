from starlette.testclient import TestClient


def test_index(client: TestClient) -> None:
    """Test if the index route works properly."""
    response = client.get("/")
    assert response.status_code == 200
    assert "RSSerpent is up & running" in response.text
