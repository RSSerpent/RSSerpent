from typing import Any, Dict

from ...utils import ratelimit


path = "/_/example/ratelimit"


@ratelimit(calls=1)
async def provider() -> Dict[str, Any]:
    """Define a basic example data provider function with rate limit."""
    return {
        "title": "Example",
        "link": "https://example.com",
        "description": "An example rsserpent plugin.",
        "items": [{"title": "Example Title", "description": "Example Description"}],
    }
