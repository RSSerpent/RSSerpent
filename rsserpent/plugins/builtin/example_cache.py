from typing import Any, Dict

from ...utils import cached


count = 0
path = "/_/example/cache"


@cached
async def provider() -> Dict[str, Any]:
    """Define a basic example data provider function with `@cached`."""
    global count
    count += 1
    return {
        "title": f"Example {count}",
        "link": "https://example.com",
        "description": "An example rsserpent plugin.",
        "items": [{"title": "Example Article", "description": "Example Content"}],
    }
