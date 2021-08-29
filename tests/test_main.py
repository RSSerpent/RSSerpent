from rsserpent.main import app


def test_index() -> None:
    """Test if the index route works properly."""
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"RSSerpent is up & running" in response.data
