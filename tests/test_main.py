from fastapi.testclient import TestClient
from importlib_metadata import entry_points

from rsserpent.main import app
from rsserpent.model import Plugin


def test_app() -> None:
    """Test the current app version."""
    assert app.version == "0.1.0"


def test_routes() -> None:
    """Test if all routes of the current app works properly."""
    client = TestClient(app)
    for entry_point in entry_points(group="rsserpent.plugins"):
        plugin: Plugin = entry_point.load()
        for path in plugin.routers:
            assert client.get(path).status_code == 200
