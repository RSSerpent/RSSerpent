import asyncio
from functools import partial, wraps
from typing import Any, Awaitable, Callable, Dict, Tuple

from hypothesis import given, settings
from hypothesis.provisional import urls
from hypothesis.strategies import builds, dictionaries, functions, just, text
from pydantic import validate_model

from rsserpent.models.plugin import Persona, Plugin, ProviderFn
from tests.conftest import Times


def force_async(fn: Callable[..., Any]) -> Callable[..., Awaitable[Any]]:
    """Convert a synchronous function to an async one.

    Derived from https://stackoverflow.com/a/50450553.
    """

    @wraps(fn)
    async def async_fn(*args: Tuple[Any, ...], **kwds: Dict[str, Any]) -> Any:
        loop = asyncio.get_event_loop()
        partial_fn = partial(fn, *args, **kwds)
        return await loop.run_in_executor(None, partial_fn)

    return async_fn


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
            name=text().map(lambda s: f"rsserpent-plugin-{s}"),
            author=builds(Persona, link=urls()),
            repository=urls(),
            prefix=just("/prefix"),
            routers=dictionaries(
                text().map(lambda s: f"/prefix/{s}"),
                functions().map(force_async),
                min_size=1,
            ),
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
        routers=dictionaries(
            text().map(lambda s: f"/prefix/{s}"),
            functions().map(force_async),
            min_size=1,
        ),
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
        name=text().map(lambda s: f"rsserpent-plugin-{s}"),
        author=builds(Persona, link=urls()),
        repository=urls(),
        prefix=just("/prefix"),
        routers=dictionaries(text().map(lambda s: f"/prefix/{s}"), functions()),
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
        if len(routers) == 0:
            assert "plugin must include at least one router." in str(e)
        else:
            assert "provider functions must be asynchronous." in str(e)

    @settings(max_examples=Times.SOME)
    @given(
        name=text().map(lambda s: f"rsserpent-plugin-{s}"),
        author=builds(Persona, link=urls()),
        repository=urls(),
        prefix=just("/prefix"),
        routers=dictionaries(text(), functions().map(force_async), min_size=1),
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
