from typing import Any, Dict

from pyquery import PyQuery

from ...utils import Browser


path = "/_/example/playwright"


async def provider() -> Dict[str, Any]:
    """Define a basic example data provider function."""
    async with Browser() as browser:
        await browser.goto("https://httpbin.org/html")
        content = await browser.content()
    dom = PyQuery(content)
    return {
        "title": "Example",
        "link": "https://example.com",
        "description": "An example rsserpent plugin.",
        "items": [{"title": dom("h1").text(), "description": dom("div > p").text()}],
    }
