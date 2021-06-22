from typing import List, Optional
from datetime import datetime

from pydantic import AnyUrl, BaseModel, HttpUrl, root_validator


class Category(BaseModel):
    name: str
    domain: Optional[str]


class Enclosure(BaseModel):
    length: int = 0
    type: str
    url: AnyUrl


class GUID(BaseModel):
    isPermaLink: bool = True
    value: str


class Image(BaseModel):
    url: HttpUrl
    title: str
    link: HttpUrl
    width: Optional[int] = 88
    height: Optional[int] = 31
    description: Optional[str]


class Source(BaseModel):
    name: str
    url: Optional[HttpUrl]


class Item(BaseModel):
    title: Optional[str]
    link: Optional[HttpUrl]
    description: Optional[str]
    author: Optional[str]
    category: Optional[List[Category]]
    comments: Optional[HttpUrl]
    enclosure: Optional[Enclosure]
    guid: Optional[GUID]
    pubDate: Optional[datetime]
    source: Optional[Source]

    @root_validator
    def validate(cls, values: dict) -> dict:  # type: ignore
        title, description = values.get("title"), values.get("description")
        if title is None and description is None:
            raise ValueError("at least one of title or description must be present")
        return values


class Feed(BaseModel):
    """
    Data model for RSS 2.0 feeds, see specification at \
    https://www.rssboard.org/rss-specification.

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
    managingEditor: Optional[str]
    webMaster: Optional[str]
    pubDate: Optional[datetime]
    lastBuildDate: Optional[datetime]
    categories: Optional[List[Category]]
    generator: Optional[str] = __package__.split(".")[0]
    docs: Optional[HttpUrl] = HttpUrl("https://www.rssboard.org/rss-specification")
    ttl: Optional[int] = 60
    image: Optional[Image]
    items: Optional[List[Item]]
