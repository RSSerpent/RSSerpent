from typing import Any, Dict, Tuple

import pytest
from hypothesis import given, settings
from hypothesis.strategies import (
    DataObject,
    booleans,
    data,
    dictionaries,
    floats,
    integers,
    lists,
    text,
    tuples,
)

from rsserpent.util.cache import CacheKey, cached, cached_with
from tests.conftest import Times


primitive = booleans() | floats() | integers() | text()


class TestCacheKey:
    """Test the `CacheKey` class."""

    @settings(max_examples=Times.THOROUGH)
    @given(
        args=tuples(primitive, primitive, primitive, lists(primitive)),
        kwds=dictionaries(text(), primitive | lists(primitive), min_size=1),
    )
    def test(self, args: Tuple[Any, ...], kwds: Dict[str, Any]) -> None:
        """
        Test if the `CacheKey` class works properly.

        * `is_primitive`, `make`, `__eq__`, `__hash__`, `__init__`
        """
        key1 = CacheKey.make(args, kwds)
        key2 = CacheKey.make(
            tuple(arg for arg in args if CacheKey.is_primitive(arg)),
            {k: v for k, v in kwds.items() if CacheKey.is_primitive(v)},
        )
        assert key1 == key2
        with pytest.raises(NotImplementedError):
            assert key1 == object()


@settings(max_examples=Times.SOME)
@given(n=integers(min_value=2, max_value=100))
def test_cached(n: int) -> None:
    """Test if `@cached` decorator works properly."""

    @cached
    def fib(n: int) -> int:
        return n if n < 2 else int(fib(n - 1) + fib(n - 2))

    assert fib(n) == fib(n - 1) + fib(n - 2)
    assert fib.cache.hits == n
    assert fib.cache.size == n + 1
    assert fib.cache.misses == n + 1


@settings(max_examples=Times.ONCE)
@given(n=integers(min_value=2, max_value=10), expire=integers(max_value=-1))
def test_cached_with_expire(n: int, expire: int) -> None:
    """Test if `@cached_with` decorator works properly, given parameter `expire`."""

    @cached_with(expire=expire)
    def fib(n: int) -> int:
        return n if n < 2 else int(fib(n - 1) + fib(n - 2))

    assert fib(n) == fib(n - 1) + fib(n - 2)
    assert fib.cache.hits == 0


@settings(max_examples=Times.SOME)
@given(data())
def test_cached_with_maxsize(data: DataObject) -> None:
    """Test if `@cached_with` decorator works properly, given parameter `maxsize`."""
    n = data.draw(integers(min_value=2, max_value=10))

    # cache size too small
    maxsize = data.draw(integers(min_value=1, max_value=n))

    @cached_with(maxsize=maxsize)
    def fib1(n: int) -> int:
        return n if n < 2 else int(fib1(n - 1) + fib1(n - 2))

    assert fib1(n) == fib1(n - 1) + fib1(n - 2)
    assert fib1.cache.size == maxsize

    # cache size suffice
    maxsize = data.draw(integers(max_value=0) | integers(min_value=n + 1))

    @cached_with(maxsize=maxsize)
    def fib2(n: int) -> int:
        return n if n < 2 else int(fib2(n - 1) + fib2(n - 2))

    assert fib2(n) == fib2(n - 1) + fib2(n - 2)
    assert fib2.cache.size == n + 1
