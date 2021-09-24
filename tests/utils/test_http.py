import pytest

from rsserpent.utils.http import HTTPClient


@pytest.mark.asyncio
async def test_http_client() -> None:
    """Test if the `http_client` context manager works properly."""
    url = "https://httpbin.org/get"
    async with HTTPClient() as client:
        response = await client.get(url)
        data = response.json()
    assert response.status_code == 200
    assert {"Host", "Referer", "User-Agent"}.issubset(set(data["headers"]))
