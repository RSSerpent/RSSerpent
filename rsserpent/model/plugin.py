from typing import TYPE_CHECKING, Callable, Dict

from pydantic import BaseModel, validator
from pydantic.class_validators import root_validator


if TYPE_CHECKING:
    EmailStr = str
    HttpUrl = str
else:
    from pydantic import EmailStr, HttpUrl


class Persona(BaseModel):
    """
    Data model for personal information.

    This could be used for documenting the author or maintainers of a certain plugin.
    """

    name: str
    link: HttpUrl
    email: EmailStr


class Plugin(BaseModel):
    """Data model for RSSerpent plugins."""

    name: str
    author: Persona
    repository: HttpUrl
    prefix: str
    routers: Dict[str, Callable]

    @root_validator
    def validate(cls, values: dict) -> dict:  # type: ignore # noqa: N805
        """Ensure all paths in `routers` starts with `prefix`."""
        prefix = values.get("prefix")
        routers = values.get("routers")
        assert prefix is not None and routers is not None
        for path in routers:
            if not path.startswith(prefix):
                raise ValueError("all path in `routers` must starts with `prefix`.")
        return values

    @validator("name")
    def validate_name(cls, name: str) -> str:  # noqa: N805
        r"""Ensure any plugin name starts with `"rsserpent-plugin-"`."""
        if not name.startswith("rsserpent-plugin-"):
            raise ValueError('plugin names must start with "rsserpent-plugin-".')
        return name

    @validator("routers")
    def validate_routers(
        cls, routers: Dict[str, Callable]  # noqa: N805
    ) -> Dict[str, Callable]:
        """Ensure `routers` is not empty."""
        if len(routers) < 1:
            raise ValueError("plugin must include at least one router.")
        return routers
