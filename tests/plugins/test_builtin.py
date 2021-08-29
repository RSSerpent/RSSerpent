from hypothesis import given, settings
from hypothesis.strategies import integers

from rsserpent import app
from tests.conftest import Times


def test_example() -> None:
    """Test the `/_/example/basic/` route."""
    with app.test_client() as client:
        response = client.get("/_/example/basic/")
        assert response.status_code == 200
        assert response.content_type == "application/xml; charset=utf-8"
        assert b"item" not in response.get_data()


@settings(max_examples=Times.SOME)
@given(n=integers(min_value=1, max_value=10))
def test_example_with_args(n: int) -> None:
    """Test the `/_/example/<int:n>/` route."""
    with app.test_client() as client:
        response = client.get(f"/_/example/{n}/")
        assert response.status_code == 200
        assert response.content_type == "application/xml; charset=utf-8"
        assert response.get_data(as_text=True).count("<item>") == n
