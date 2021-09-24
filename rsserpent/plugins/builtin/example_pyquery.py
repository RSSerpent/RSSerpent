from typing import Any, Dict

from pyquery import PyQuery

from ...utils import HTTPClient


path = "/_/example/pyquery"


async def provider() -> Dict[str, Any]:
    """Define a basic example data provider function."""
    async with HTTPClient() as client:
        response = await client.get("https://httpbin.org/html")
    dom = PyQuery(response.text)
    return {
        "title": "Example",
        "link": "https://example.com",
        "description": "An example rsserpent plugin.",
        "items": [{"title": dom("h1").text(), "description": dom("div > p").text()}],
    }
