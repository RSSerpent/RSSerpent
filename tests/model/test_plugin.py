from typing import Callable, Dict, List

import pytest
from hypothesis import given, infer, settings
from hypothesis.provisional import urls
from hypothesis.strategies import (
    builds,
    dictionaries,
    from_regex,
    functions,
    lists,
    text,
)
from pydantic import ValidationError

from rsserpent.model.plugin import Persona, Plugin
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

    @settings(max_examples=Times.SOME)
    @given(
        builds(
            Plugin,
            name=from_regex(r"^rsserpent-plugin-\w+"),
            description=infer,
            author=builds(Persona, link=urls()),
            maintainers=lists(builds(Persona, link=urls())),
            repository=urls(),
            routers=dictionaries(text(), functions(), min_size=1),
        )
    )
    def test(self, plugin: Plugin) -> None:
        """Test if the `Plugin` class works properly."""
        assert plugin is not None

    @settings(max_examples=Times.ONCE)
    @given(
        name=text(),
        author=builds(Persona, link=urls()),
        maintainers=lists(builds(Persona, link=urls())),
        repository=urls(),
        routers=dictionaries(text(), functions(), min_size=1),
    )
    def test_name_validation(
        self,
        name: str,
        author: Persona,
        maintainers: List[Persona],
        repository: str,
        routers: Dict[str, Callable],
    ) -> None:
        """Test if the `Plugin` class validates `name` properly."""
        with pytest.raises(ValidationError):
            Plugin(
                name=name,
                author=author,
                maintainers=maintainers,
                repository=repository,
                routers=routers,
            )

    @settings(max_examples=Times.ONCE)
    @given(
        name=from_regex(r"^rsserpent-plugin-\w+"),
        author=builds(Persona, link=urls()),
        maintainers=lists(builds(Persona, link=urls())),
        repository=urls(),
        routers=dictionaries(text(), functions(), max_size=0),
    )
    def test_routers_validation(
        self,
        name: str,
        author: Persona,
        maintainers: List[Persona],
        repository: str,
        routers: Dict[str, Callable],
    ) -> None:
        """Test if the `Plugin` class validates `routers` properly."""
        with pytest.raises(ValidationError):
            Plugin(
                name=name,
                author=author,
                maintainers=maintainers,
                repository=repository,
                routers=routers,
            )
