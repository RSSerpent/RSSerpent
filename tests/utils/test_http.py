import pytest

from rsserpent.utils.http import Browser, HTTPClient


@pytest.mark.asyncio
async def test_browser() -> None:
    """Test if the `Browser` context manager works properly."""
    async with Browser() as browser:
        await browser.goto("https://httpbin.org/html")
        assert "Herman Melville - Moby-Dick" in await browser.content()


@pytest.mark.asyncio
async def test_http_client() -> None:
    """Test if the `http_client` context manager works properly."""
    url = "https://httpbin.org/get"
    async with HTTPClient() as client:
        response = await client.get(url)
        data = response.json()
    assert response.status_code == 200
    assert {"Host", "Referer", "User-Agent"}.issubset(set(data["headers"]))
