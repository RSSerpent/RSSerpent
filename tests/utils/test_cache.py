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

from rsserpent.utils.cache import CacheKey, cached, get_cache
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
        """Test if the `CacheKey` class works properly.

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


@pytest.mark.asyncio
@settings(max_examples=Times.SOME)
@given(n=integers(min_value=2, max_value=100))
async def test_cached(n: int) -> None:
    """Test if `@cached` decorator works properly."""

    @cached
    async def fib(n: int) -> int:
        return n if n < 2 else await fib(n - 1) + await fib(n - 2)

    assert await fib(n) == await fib(n - 1) + await fib(n - 2)

    cache = get_cache(fib)
    assert cache is not None
    assert cache.hits == n
    assert cache.size == n + 1
    assert cache.misses == n + 1


@pytest.mark.asyncio
@settings(max_examples=Times.ONCE)
@given(n=integers(min_value=2, max_value=10), expire=integers(max_value=-1))
async def test_cached_with_expire(n: int, expire: int) -> None:
    """Test if `@cached` decorator works properly, given parameter `expire`."""

    @cached(expire=expire)
    async def fib(n: int) -> int:
        return n if n < 2 else await fib(n - 1) + await fib(n - 2)

    assert await fib(n) == await fib(n - 1) + await fib(n - 2)

    cache = get_cache(fib)
    assert cache is not None
    assert cache.hits == 0


@pytest.mark.asyncio
@settings(max_examples=Times.SOME)
@given(data())
async def test_cached_with_maxsize(data: DataObject) -> None:
    """Test if `@cached` decorator works properly, given parameter `maxsize`."""
    n = data.draw(integers(min_value=2, max_value=10))

    # cache size too small
    maxsize = data.draw(integers(min_value=1, max_value=n))

    @cached(maxsize=maxsize)
    async def fib1(n: int) -> int:
        return n if n < 2 else await fib1(n - 1) + await fib1(n - 2)

    assert await fib1(n) == await fib1(n - 1) + await fib1(n - 2)

    cache = get_cache(fib1)
    assert cache is not None
    assert cache.size == maxsize

    # cache size suffice
    maxsize = data.draw(integers(max_value=0) | integers(min_value=n + 1))

    @cached(maxsize=maxsize)
    async def fib2(n: int) -> int:
        return n if n < 2 else await fib2(n - 1) + await fib2(n - 2)

    assert await fib2(n) == await fib2(n - 1) + await fib2(n - 2)

    cache = get_cache(fib2)
    assert cache is not None
    assert cache.size == n + 1
