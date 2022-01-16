import asyncio
from functools import partial, wraps
from typing import Any, Awaitable, Callable, Dict, Tuple

from hypothesis import given, settings
from hypothesis.provisional import urls
from hypothesis.strategies import builds, dictionaries, functions, just, text
from pydantic import validate_model

from rsserpent.models.plugin import Persona, Plugin, PluginModelError, ProviderFn
from tests.conftest import Times


def to_async(fn: Callable[..., Any]) -> Callable[..., Awaitable[Any]]:
    """Convert a synchronous function to an async one.

    Derived from https://stackoverflow.com/a/50450553.
    """

    @wraps(fn)
    async def async_fn(*args: Tuple[Any, ...], **kwds: Dict[str, Any]) -> Any:
        loop = asyncio.get_event_loop()
        partial_fn = partial(fn, *args, **kwds)
        return await loop.run_in_executor(None, partial_fn)

    return async_fn


class TestPlugin:
    """Test the `Plugin` class."""

    @settings(max_examples=Times.SOME)
    @given(
        name=text(),
        author=builds(Persona),
        repository=urls(),
        prefix=just("/prefix"),
        routers=dictionaries(
            text().map(lambda s: f"/prefix/{s}"),
            functions().map(to_async),
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
        assert PluginModelError.unexpected_plugin_name in str(e)

    @settings(max_examples=Times.SOME)
    @given(
        name=text().map(lambda s: f"rsserpent-plugin-{s}"),
        author=builds(Persona),
        repository=urls(),
        prefix=just("/prefix"),
        routers=dictionaries(
            text().map(lambda s: f"/prefix/{s}"), functions(), min_size=1
        ),
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
        assert PluginModelError.provider_not_async in str(e)

        _, _, e = validate_model(
            Plugin,
            {
                "name": name,
                "author": author,
                "repository": repository,
                "prefix": prefix,
                "routers": {},
            },
        )
        assert e is not None
        assert PluginModelError.empty_router in str(e)

    @settings(max_examples=Times.SOME)
    @given(
        name=text().map(lambda s: f"rsserpent-plugin-{s}"),
        author=builds(Persona),
        repository=urls(),
        prefix=just("/prefix"),
        routers=dictionaries(text(), functions().map(to_async), min_size=1),
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
        assert PluginModelError.unexpected_router_path in str(e)
