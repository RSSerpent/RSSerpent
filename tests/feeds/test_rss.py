import pytest
from hypothesis import given, infer, settings
from hypothesis.provisional import urls
from pydantic import ValidationError

from rsserpent.feeds.rss import Category


class TestCategory:
    """Test the `Category` class."""

    @settings(max_examples=1)
    @given(name=infer, domain=urls())
    def test(self, name: str, domain: str) -> None:
        """Test if the `Category` class operates normally."""
        assert Category(name=name)
        assert Category(name=name, domain=domain)

    @settings(max_examples=5)
    @given(name=infer, domain=infer)
    def test_validation(self, name: str, domain: str) -> None:
        """Test url validation of the `Category` class."""
        with pytest.raises(ValidationError):
            Category(name=name, domain=domain)
