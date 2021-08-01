import os
import time
from collections import OrderedDict
from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional, Tuple


CACHE_EXPIRE = int(os.environ.get("CACHE_EXPIRE", 60 * 60))


class CacheKey:
    """Hashed function parameters that could be used as dictionary keys."""

    __slots__ = "hashvalue"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CacheKey):
            raise NotImplementedError
        return self.hashvalue == other.hashvalue

    def __hash__(self) -> int:
        return self.hashvalue

    def __init__(self, key: Tuple[Any, ...]) -> None:
        self.hashvalue = hash(key)

    @classmethod
    def make(cls, args: Tuple[Any, ...], kwds: Dict[str, Any]) -> "CacheKey":
        """
        Create a `CacheKey` instance from function parameters.

        Note that parameters of non-primitive types are discarded.
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

    @staticmethod
    def is_primitive(o: object) -> bool:
        """Determine whether an object is of primitive type."""
        return type(o) in (bool, float, int, str)


@dataclass
class CacheValue:
    """Cached function return value with a expiring timestamp."""

    expired: float
    data: Any


class CachedFn:
    """Function whose results are (LRU) cached with a expiring timestamp."""

    __slots__ = ("cache", "expire", "fn", "maxsize")

    def __init__(self, fn: Callable[..., Any], *, expire: int, maxsize: int) -> None:
        self.cache = LRUCache(maxsize=maxsize)
        self.expire = expire
        self.fn = fn

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
        Delegate function calls to the original `fn`.

        Cached results will be returned if cache hit, otherwise
        (missing/expired) `fn` will be invoked and its result will be cached.
        """
        key = CacheKey.make(args, kwds)
        value = self.cache[key]
        # cache miss/expired
        if value is None:
            result = self.fn(*args, **kwds)
            self.cache[key] = CacheValue(expired=time.time() + self.expire, data=result)
            return result
        return value.data


class LRUCache(OrderedDict):  # type: ignore[type-arg]
    """Least Recently Used (LRU) cache."""

    def __init__(self, maxsize: int) -> None:
        self.maxsize = maxsize if maxsize > 0 else float("inf")
        self.hits, self.misses = 0, 0
        super().__init__()

    def __getitem__(self, key: CacheKey) -> Optional[CacheValue]:
        if key not in self:
            return None
        value: CacheValue = super().__getitem__(key)
        if value.expired < time.time():
            return None
        self.move_to_end(key)
        self.hits += 1
        return value

    def __setitem__(self, key: CacheKey, value: CacheValue) -> None:
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


def cached(fn: Callable[..., Any]) -> CachedFn:
    """Cache function results."""
    return CachedFn(fn, expire=CACHE_EXPIRE, maxsize=0)


def cached_with(
    *, expire: int = CACHE_EXPIRE, maxsize: int = 0
) -> Callable[[Callable[..., Any]], CachedFn]:
    """Cache function results with customizable `expire` & `maxsize`."""
    return lambda fn: CachedFn(fn, expire=expire, maxsize=maxsize)
