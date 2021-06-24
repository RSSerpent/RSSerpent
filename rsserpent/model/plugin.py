from typing import TYPE_CHECKING, Callable, Dict, List, Optional

from pydantic import BaseModel, EmailStr, validator


if TYPE_CHECKING:
    HttpUrl = str  # pragma: no cover
else:
    from pydantic import HttpUrl


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
    description: Optional[str]
    author: Persona
    maintainers: List[Persona]
    repository: HttpUrl
    routers: Dict[str, Callable]

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
