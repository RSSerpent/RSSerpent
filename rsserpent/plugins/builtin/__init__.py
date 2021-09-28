from ...models import Persona, Plugin
from . import (
    example,
    example_cache,
    example_httpx,
    example_pyppeteer,
    example_pyquery,
    example_ratelimit,
    example_with_args,
)


plugin = Plugin(
    name="rsserpent-plugin-builtin",
    author=Persona(
        name="queensferryme",
        link="https://github.com/queensferryme",
        email="queensferry.me@gmail.com",
    ),
    repository="https://github.com/RSSerpent/RSSerpent",
    prefix="/_",
    routers={
        example.path: example.provider,
        example_cache.path: example_cache.provider,
        example_httpx.path: example_httpx.provider,
        example_pyppeteer.path: example_pyppeteer.provider,
        example_pyquery.path: example_pyquery.provider,
        example_ratelimit.path: example_ratelimit.provider,
        example_with_args.path: example_with_args.provider,
    },
)

__all__ = ("plugin",)
