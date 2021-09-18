import os
import threading
import time
from collections import OrderedDict
from dataclasses import dataclass
from functools import partial, wraps
from typing import (
    Any,
    Awaitable,
    Callable,
    Dict,
    Optional,
    Tuple,
    TypeVar,
    Union,
    cast,
    overload,
)


__all__ = ("cached",)

CACHE_EXPIRE = int(os.environ.get("CACHE_EXPIRE", 60 * 60))

AsyncFn = TypeVar("AsyncFn", bound=Callable[..., Awaitable[Any]])


class CacheKey:
    """Hashed function parameters that could be used as dictionary keys.

    This module provides `@cached` & `@cached_with` decorators for caching function
    results. Cache exists as key-value pairs. The parameters of each function
    invocation are converted to a tuple and then hashed, so that results of different
    function invocations (e.g. `fn(1)` & `fn(2)`) could be differentiated and
    separately cached.

    Attributes:
        hashvalue: The hashed value of function parameters.
    """

    __slots__ = "hashvalue"

    def __init__(self, key: Tuple[Any, ...]) -> None:
        self.hashvalue = hash(key)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CacheKey):
            raise NotImplementedError()
        return self.hashvalue == other.hashvalue

    def __hash__(self) -> int:
        return self.hashvalue

    @staticmethod
    def is_primitive(o: object) -> bool:
        """Determine whether an object is of primitive type."""
        return type(o) in (bool, float, int, str)

    @classmethod
    def make(cls, args: Tuple[Any, ...], kwds: Dict[str, Any]) -> "CacheKey":
        """Create a `CacheKey` instance from any function parameters.

        Note that parameters of non-primitive types are discarded.

        Args:
            args: Positional arguments in function parameters.
            kwds: Keyword arguments in function parameters.

        Returns:
            The created `CacheKey` instance.
        """
        key = []
        # positional arguments
        for argument in args:
            if cls.is_primitive(argument):
                key.append(argument)
        # keyword arguments
        for pair in sorted(kwds.items()):
            if cls.is_primitive(pair[1]):
                key.append(pair)
        return CacheKey(tuple(key))


@dataclass
class CacheValue:
    """Cached function results with a expiring timestamp."""

    expired: float
    data: Any


class LRUCache(OrderedDict):  # type: ignore[type-arg]
    """Least Recently Used (LRU) cache.

    Attributes:
        hits: The number of cache hits.
        maxsize: The maximum capacity of the LRU cache.
        misses: The number of cache misses.
    """

    def __init__(self, maxsize: int) -> None:
        self.maxsize = maxsize if maxsize > 0 else float("inf")
        self.hits, self.misses = 0, 0
        self.lock = threading.RLock()
        super().__init__()

    def __getitem__(self, key: CacheKey) -> Optional[CacheValue]:
        """Get cache value by key.

        In case of cache miss / expire, `None` is returned. Otherwise the cached value
        is returned and moved to the end of the list.
        """
        if key not in self:
            return None
        value: CacheValue = super().__getitem__(key)
        if value.expired < time.monotonic():
            return None
        self.move_to_end(key)
        self.hits += 1
        return value

    def __setitem__(self, key: CacheKey, value: CacheValue) -> None:
        """Set a cache (key, value) pair.

        The `__setitem__` is called only when a cache miss / expire happens. In case of
        cache expire, the existing `key` must be moved to the end of the list. In case
        cache maximum capacity is reached, the first (thus least recently used) cache
        item is deleted.
        """
        with self.lock:
            if key in self:
                self.move_to_end(key)
            super().__setitem__(key, value)
            self.misses += 1
            if len(self) > self.maxsize:
                # do not use `self.popitem`
                del self[next(iter(self))]

    @property
    def size(self) -> int:
        """Return the current size of the cache."""
        return super().__len__()


def decorator(fn: AsyncFn, *, expire: int, maxsize: int) -> AsyncFn:
    """Cache decorator."""
    cache = LRUCache(maxsize=maxsize)

    @wraps(fn)
    async def wrapper(*args: Tuple[Any, ...], **kwds: Dict[str, Any]) -> Any:
        """Wrap the original async `fn`.

        Cached results will be returned if cache hit, otherwise
        (missing/expired) `fn` will be invoked and its result will be cached.

        Args:
            args: Positional arguments in function parameters.
            kwds: Keyword arguments in function parameters.

        Returns:
            The (maybe cached) result of `fn(*args, **kwds)`.
        """
        key = CacheKey.make(args, kwds)
        value = cache[key]
        # cache miss/expired
        if value is None:
            result = await fn(*args, **kwds)
            cache[key] = CacheValue(expired=time.monotonic() + expire, data=result)
            return result
        return value.data

    wrapper.__dict__["cache"] = cache
    wrapper.__dict__["expire"] = expire
    return cast(AsyncFn, wrapper)


@overload
def cached(fn: AsyncFn) -> AsyncFn:
    ...  # pragma: no cover


@overload
def cached(
    *, expire: int = CACHE_EXPIRE, maxsize: int = 0
) -> Callable[[AsyncFn], AsyncFn]:
    ...  # pragma: no cover


def cached(
    fn: Optional[AsyncFn] = None, *, expire: int = CACHE_EXPIRE, maxsize: int = 0
) -> Union[AsyncFn, Callable[[AsyncFn], AsyncFn]]:
    """Cache function results."""
    if fn is not None:
        return decorator(fn, expire=expire, maxsize=maxsize)
    return partial(decorator, expire=expire, maxsize=maxsize)


def get_cache(fn: AsyncFn) -> Optional[LRUCache]:
    return fn.__dict__.get("cache")
