import threading
import time
from functools import partial, wraps
from typing import Any, Awaitable, Callable, Dict, Tuple, TypeVar, cast


AsyncFn = TypeVar("AsyncFn", bound=Callable[..., Awaitable[Any]])


class RateLimitError(Exception):
    """Exception for function rate limit exceeded."""

    def __init__(self, fn: str, called: int, max_calls: int) -> None:
        """Populate `RateLimitError` error message."""
        super().__init__(f"function {fn} ratelimit exceeded ({called} > {max_calls}).")


def decorator(fn: AsyncFn, *, calls: int, period: float) -> AsyncFn:
    """Rate limit decorator."""
    called = 0
    last_reset_time = time.monotonic()
    lock = threading.RLock()
    max_calls = calls

    @wraps(fn)
    async def wrapper(*args: Tuple[Any, ...], **kwds: Dict[str, Any]) -> Any:
        """Wrap the original async `fn`.

        At most `calls` invocations are allow within `period` seconds.

        Args:
            args: Positional arguments in function parameters.
            kwds: Keyword arguments in function parameters.

        Returns:
            The result of `fn(*args, **kwds)`, if rate limit not exceeded.

        Raises:
            RateLimitError: function rate limit exceeded.
        """
        nonlocal called, last_reset_time, max_calls
        with lock:
            current_time = time.monotonic()
            # reset if the period is over
            if current_time > last_reset_time + period:
                called = 0
                last_reset_time = current_time
            called += 1
            # raise if rate limit exceeded
            if called > max_calls:
                raise RateLimitError(
                    f"{fn.__module__}.{fn.__name__}", called, max_calls
                )
            return await fn(*args, **kwds)

    return cast(AsyncFn, wrapper)


def ratelimit(*, calls: int, period: float = 3600) -> Callable[[AsyncFn], AsyncFn]:
    """Rate limit function calls.

    Args:
        calls: number of function calls allow within one period.
        period: length of the period, in seconds.

    Returns:
        A decorator that accepts an async function and returns a rate limited one.
    """
    return partial(decorator, calls=calls, period=period)
