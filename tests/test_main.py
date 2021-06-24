from rsserpent.main import app


def test_app() -> None:
    """Test the current app version."""
    assert app.version == "0.1.0"
