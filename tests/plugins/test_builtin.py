from hypothesis import given, settings
from hypothesis.strategies import integers
from starlette.testclient import TestClient

from rsserpent import app
from tests.conftest import Times


def test_example() -> None:
    """Test the `/_/example` route."""
    client = TestClient(app)
    response = client.get("/_/example")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"
    assert "<item>" not in response.text


@settings(max_examples=Times.SOME)
@given(n=integers(min_value=1, max_value=10))
def test_example_with_args(n: int) -> None:
    """Test the `/_/example/{n:int}` route."""
    client = TestClient(app)
    response = client.get(f"/_/example/{n}")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"
    assert response.text.count("<item>") == n
