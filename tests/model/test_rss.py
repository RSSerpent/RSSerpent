from typing import Optional

from hypothesis import given, infer, settings
from hypothesis.provisional import urls
from hypothesis.strategies import builds, fixed_dictionaries, lists, none, text
from pydantic import HttpUrl, ValidationError

from rsserpent.model.rss import Category, Enclosure, Feed, GUID, Image, Item, Source
from tests.conftest import Times


class TestCategory:
    """Test the `Category` class."""

    @settings(max_examples=Times.SOME)
    @given(builds(Category, url=urls() | none()))
    def test(self, category: Category) -> None:
        """Test if the `Category` class works properly."""
        assert category is not None
        assert isinstance(category.domain, HttpUrl) or (category.domain is None)


class TestEnclosure:
    """Test the `Enclosure` class."""

    @settings(max_examples=Times.ONCE)
    @given(builds(Enclosure, url=urls()))
    def test(self, enclosure: Enclosure) -> None:
        """Test if the `Enclosure` class works properly."""
        assert enclosure is not None

    @settings(max_examples=Times.SOME)
    @given(type=infer, url=urls())
    def test_default_length(self, type: str, url: str) -> None:
        """Test the default value of `length` in the `Enclosure` class."""
        assert Enclosure(type=type, url=url).length == 0


class TestGUID:
    """Test the `GUID` class."""

    @settings(max_examples=Times.ONCE)
    @given(builds(GUID))
    def test(self, guid: GUID) -> None:
        """Test if the `GUID` class works properly."""
        assert guid is not None

    @settings(max_examples=Times.SOME)
    @given(value=infer)
    def test_default_is_perma_link(self, value: str) -> None:
        """Test the default value of `is_perma_link` in the `GUID` class."""
        assert GUID(value=value).is_perma_link is True


class TestImage:
    """Test the `Image` class."""

    @settings(max_examples=Times.ONCE)
    @given(builds(Image, url=urls(), link=urls()))
    def test(self, image: Image) -> None:
        """Test if the `Image` class works properly."""
        assert image is not None

    @settings(max_examples=Times.SOME)
    @given(url=urls(), title=infer, link=urls(), description=infer)
    def test_default_width_and_height(
        self, url: str, title: str, link: str, description: Optional[str]
    ) -> None:
        """Test the default value of `width` & `height` in the `Image` class."""
        image = Image(url=url, title=title, link=link, description=description)
        assert image.width == 88
        assert image.height == 31


class TestSource:
    """Test the `Source` class."""

    @settings(max_examples=Times.SOME)
    @given(builds(Source, url=urls() | none()))
    def test(self, source: Source) -> None:
        """Test if the `Source` class works properly."""
        assert source is not None
        assert isinstance(source.url, HttpUrl) or (source.url is None)


class TestItem:
    """Test the `Item` class."""

    @settings(max_examples=Times.SOME)
    @given(
        builds(
            Item,
            title=text(),
            link=urls() | none(),
            description=infer,
            author=infer,
            categories=lists(fixed_dictionaries({"name": text()})) | none(),
            comments=urls() | none(),
            enclosure=builds(Enclosure, url=urls()) | none(),
            guid=builds(GUID) | none(),
            pub_date=infer,
            source=builds(Source, url=urls() | none()) | none(),
        )
    )
    def test(self, item: Item) -> None:
        """Test if the `Item` class works properly."""
        assert item is not None

    @settings(max_examples=Times.THOROUGH)
    @given(title=infer, description=infer)
    def test_validation(self, title: Optional[str], description: Optional[str]) -> None:
        """Test if the `@root_validator` of `Item` class works properly."""
        try:
            Item(title=title, description=description)
        except ValidationError:
            assert title is None and description is None


class TestFeed:
    """Test the `Feed` class."""

    @settings(max_examples=Times.SOME)
    @given(
        builds(
            Feed,
            title=infer,
            link=urls(),
            description=infer,
            language=infer,
            copyright=infer,
            managing_editor=infer,
            web_master=infer,
            pub_date=infer,
            last_build_date=infer,
            categories=lists(fixed_dictionaries({"name": text()})) | none(),
            generator=infer,
            docs=urls() | none(),
            ttl=infer,
            image=builds(Image, url=urls(), link=urls()) | none(),
            items=lists(fixed_dictionaries({"title": text()})) | none(),
        )
    )
    def test(self, feed: Feed) -> None:
        """Test if the `Feed` lass works properly."""
        assert feed is not None

    @settings(max_examples=Times.SOME)
    @given(title=infer, link=urls(), description=infer)
    def test_default_values(self, title: str, link: str, description: str) -> None:
        """Test the default value of `ttl`in the `Feed` class."""
        assert Feed(title=title, link=link, description=description).ttl == 60
