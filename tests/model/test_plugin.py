from typing import Dict

from hypothesis import given, settings
from hypothesis.provisional import urls
from hypothesis.strategies import (
    builds,
    dictionaries,
    from_regex,
    functions,
    just,
    text,
)
from pydantic import validate_model

from rsserpent.model.plugin import Persona, Plugin, ProviderFn
from tests.conftest import Times


class TestPersona:
    """Test the `Persona` class."""

    @settings(max_examples=Times.SOME)
    @given(builds(Persona, link=urls()))
    def test(self, persona: Persona) -> None:
        """Test if the `Persona` class works properly."""
        assert "@" in persona.email


class TestPlugin:
    """Test the `Plugin` class."""

    @settings(max_examples=Times.ONCE)
    @given(
        builds(
            Plugin,
            name=from_regex(r"^rsserpent-plugin-\w+"),
            author=builds(Persona, link=urls()),
            repository=urls(),
            prefix=just("/prefix"),
            routers=dictionaries(from_regex(r"^/prefix/\w+"), functions(), min_size=1),
        )
    )
    def test(self, plugin: Plugin) -> None:
        """Test if the `Plugin` class works properly."""
        assert plugin is not None

    @settings(max_examples=Times.SOME)
    @given(
        name=text(),
        author=builds(Persona, link=urls()),
        repository=urls(),
        prefix=just("/prefix"),
        routers=dictionaries(from_regex(r"^/prefix/\w+"), functions(), min_size=1),
    )
    def test_name_validation(
        self,
        name: str,
        author: Persona,
        repository: str,
        prefix: str,
        routers: Dict[str, ProviderFn],
    ) -> None:
        """Test if the `Plugin` class validates `name` properly."""
        _, _, e = validate_model(
            Plugin,
            {
                "name": name,
                "author": author,
                "repository": repository,
                "prefix": prefix,
                "routers": routers,
            },
        )
        assert e is not None
        assert 'plugin names must start with "rsserpent-plugin-".' in str(e)

    @settings(max_examples=Times.SOME)
    @given(
        name=from_regex(r"^rsserpent-plugin-\w+"),
        author=builds(Persona, link=urls()),
        repository=urls(),
        prefix=just("/prefix"),
        routers=dictionaries(text(), functions(), max_size=0),
    )
    def test_routers_validation(
        self,
        name: str,
        author: Persona,
        repository: str,
        prefix: str,
        routers: Dict[str, ProviderFn],
    ) -> None:
        """Test if the `Plugin` class validates `routers` properly."""
        _, _, e = validate_model(
            Plugin,
            {
                "name": name,
                "author": author,
                "repository": repository,
                "prefix": prefix,
                "routers": routers,
            },
        )
        assert e is not None
        assert "plugin must include at least one router." in str(e)

    @settings(max_examples=Times.SOME)
    @given(
        name=from_regex(r"^rsserpent-plugin-\w+"),
        author=builds(Persona, link=urls()),
        repository=urls(),
        prefix=just("/prefix"),
        routers=dictionaries(text(), functions(), min_size=1),
    )
    def test_validation(
        self,
        name: str,
        author: Persona,
        repository: str,
        prefix: str,
        routers: Dict[str, ProviderFn],
    ) -> None:
        """Test if the `@root_validator` of `Item` class works properly."""
        _, _, e = validate_model(
            Plugin,
            {
                "name": name,
                "author": author,
                "repository": repository,
                "prefix": prefix,
                "routers": routers,
            },
        )
        assert e is not None
        assert "all path in `routers` must starts with `prefix`." in str(e)
