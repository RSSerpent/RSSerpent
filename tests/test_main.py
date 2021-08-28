from rsserpent.main import app
from rsserpent.plugins.builtin import plugin


def test_index_route() -> None:
    """Test if the index route works properly."""
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"RSSerpent is up & running" in response.data


def test_plugin_routes() -> None:
    """Test if all (builtin) plugin routes works properly."""
    with app.test_client() as client:
        for path in plugin.routers:
            response = client.get(path)
            assert response.status_code == 200
            assert b'<?xml version="1.0"?>' in response.data
