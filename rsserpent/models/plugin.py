import asyncio
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Dict, Optional

from pydantic import BaseModel, validator
from pydantic.class_validators import root_validator


if TYPE_CHECKING:
    EmailStr = str
    HttpUrl = str
else:
    from pydantic import EmailStr, HttpUrl


ProviderFn = Callable[..., Awaitable[Dict[str, Any]]]


class PluginModelError(ValueError):
    """Exception for `Plugin` model validation error."""

    plugin_name_prefix = 'plugin names must start with "rsserpent-plugin-".'
    provider_not_async = "provider functions must be asynchronous."
    router_path_prefix = "all path in `routers` must starts with `prefix`."
    router_not_empty = "plugin must include at least one router."


class Persona(BaseModel):
    """Data model for plugin authors' personal information."""

    name: str
    link: HttpUrl
    email: EmailStr


class Plugin(BaseModel):
    """Data model for a RSSerpent plugin."""

    name: str
    author: Persona
    repository: HttpUrl
    prefix: str
    routers: Dict[str, ProviderFn]

    @root_validator
    def validate(  # type: ignore[override]
        cls, values: Dict[str, Any]  # noqa: N805
    ) -> Dict[str, Any]:
        """Ensure all paths in `routers` starts with `prefix`."""
        prefix: Optional[str] = values.get("prefix")
        routers: Optional[Dict[str, ProviderFn]] = values.get("routers")
        assert prefix is not None and routers is not None
        for path in routers:
            if not path.startswith(prefix):
                raise PluginModelError(PluginModelError.router_path_prefix)
        return values

    @validator("name")
    def validate_name(cls, name: str) -> str:  # noqa: N805
        r"""Ensure any plugin name starts with `"rsserpent-plugin-"`."""
        if not name.startswith("rsserpent-plugin-"):
            raise PluginModelError(PluginModelError.plugin_name_prefix)
        return name

    @validator("routers")
    def validate_routers(
        cls, routers: Dict[str, ProviderFn]  # noqa: N805
    ) -> Dict[str, ProviderFn]:
        """Ensure `routers` is not empty & all provider functions are async."""
        if len(routers) < 1:
            raise PluginModelError(PluginModelError.router_not_empty)
        for provider in routers.values():
            if not asyncio.iscoroutinefunction(provider):
                raise PluginModelError(PluginModelError.provider_not_async)
        return routers
