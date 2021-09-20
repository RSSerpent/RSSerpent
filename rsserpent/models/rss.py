from typing import TYPE_CHECKING, Any, Dict, List, Optional

import arrow
from arrow import Arrow
from pydantic import BaseModel, Field, root_validator


if TYPE_CHECKING:
    AnyUrl = str
    HttpUrl = str
else:
    from pydantic import AnyUrl, HttpUrl


class RSSModelError(ValueError):
    """Exception for `Feed` model validation error."""

    title_or_description = "at least one of <title> or <description> must be present."


class Category(BaseModel):
    """Data model for the `<category>` field in an RSS 2.0 feed."""

    name: str
    domain: Optional[HttpUrl]


class Enclosure(BaseModel):
    """Data model for the `<enclosure>` field in an RSS 2.0 feed."""

    length: int = 0
    type: str
    url: AnyUrl


class Guid(BaseModel):
    """Data model for the `<guid>` field in an RSS 2.0 feed."""

    is_perma_link: bool = True
    value: str


class Image(BaseModel):
    """Data model for the `<image>` field in an RSS 2.0 feed."""

    url: HttpUrl
    title: str
    link: HttpUrl
    width: Optional[int] = 88
    height: Optional[int] = 31
    description: Optional[str]


class Source(BaseModel):
    """Data model for the `<source>` field in an RSS 2.0 feed."""

    name: str
    url: Optional[HttpUrl]


class Item(BaseModel):
    """Data model for the `<item>` field in an RSS 2.0 feed."""

    title: Optional[str]
    link: Optional[HttpUrl]
    description: Optional[str]
    author: Optional[str]
    categories: Optional[List[Category]]
    comments: Optional[HttpUrl]
    enclosure: Optional[Enclosure]
    guid: Optional[Guid]
    pub_date: Optional[Arrow]
    source: Optional[Source]

    class Config:  # noqa: D106
        arbitrary_types_allowed = True

    @root_validator
    def validate(  # type: ignore[override]
        cls, values: Dict[str, Any]  # noqa: N805
    ) -> Dict[str, Any]:
        """Ensure at least one of `<title>` or `<description>` is present."""
        title, description = values.get("title"), values.get("description")
        if title is None and description is None:
            raise RSSModelError(RSSModelError.title_or_description)
        return values


class Feed(BaseModel):
    """Data model for RSS 2.0 feeds.

    See specification at https://www.rssboard.org/rss-specification.
    Note that some rarely used fields are not implemented:
    * `<cloud>`
    * `<rating>`
    * `<textInput>`
    * `<skipHours>`
    * `<skipDays>`
    """

    title: str
    link: HttpUrl
    description: str
    language: Optional[str]
    copyright: Optional[str]
    managing_editor: Optional[str]
    web_master: Optional[str]
    pub_date: Optional[Arrow] = Field(default_factory=arrow.utcnow)
    last_build_date: Optional[Arrow] = Field(default_factory=arrow.utcnow)
    categories: Optional[List[Category]]
    generator: Optional[str] = __package__.split(".")[0]
    docs: Optional[HttpUrl] = "https://www.rssboard.org/rss-specification"
    ttl: Optional[int] = 60
    image: Optional[Image]
    items: Optional[List[Item]]

    class Config:  # noqa: D106
        arbitrary_types_allowed = True
