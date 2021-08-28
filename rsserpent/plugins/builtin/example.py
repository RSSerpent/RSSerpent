from typing import Any, Dict


path = "/_/example"


def provider(_args: Dict[str, Any], _qs: Dict[str, str]) -> Dict[str, Any]:
    """Define a basic example data provider function."""
    return {
        "title": "Example",
        "link": "https://example.com",
        "description": "An example rsserpent plugin.",
    }
