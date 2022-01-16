from typing import Optional

from hypothesis import given, infer, settings
from pydantic import validate_model

from rsserpent.models.rss import Item, RSSModelError
from tests.conftest import Times


class TestItem:
    """Test the `Item` class."""

    @settings(max_examples=Times.THOROUGH)
    @given(title=infer, description=infer)
    def test_validation(self, title: Optional[str], description: Optional[str]) -> None:
        """Test if the `@root_validator` of `Item` class works properly."""
        _, _, e = validate_model(
            Item,
            {
                "title": title,
                "description": description,
            },
        )
        if e is not None:
            assert title is None and description is None
            assert RSSModelError.empty_title_and_description in str(e)
