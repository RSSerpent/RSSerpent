from fastapi.testclient import TestClient
from importlib_metadata import entry_points

from rsserpent.main import app
from rsserpent.model import Plugin


def test_app() -> None:
    """Test the current app version."""
    assert app.version == "0.1.0"


def test_index_route() -> None:
    """Test if the index route works properly."""
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "RSSerpent is up & running" in response.text


def test_plugin_routes() -> None:
    """Test if all plugin routes works properly."""
    client = TestClient(app)
    for entry_point in entry_points(group="rsserpent.plugins"):
        plugin: Plugin = entry_point.load()
        for path in plugin.routers:
            response = client.get(path)
            assert response.status_code == 200
            assert '<?xml version="1.0"?>' in response.text
