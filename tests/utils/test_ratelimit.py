import time

import pytest

from rsserpent.utils.ratelimit import RateLimitError, ratelimit


@ratelimit(calls=3, period=100)
async def rick() -> str:
    """Rickrolling!"""
    return "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


async def test_ratelimit(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test if `@ratelimit` decorator works properly."""
    for _ in range(3):
        assert "dQw4w9WgXcQ" in await rick()
    with pytest.raises(RateLimitError):
        await rick()

    current_time = time.monotonic()
    with monkeypatch.context() as m:
        m.setattr(time, "monotonic", lambda: current_time + 100)
        assert "dQw4w9WgXcQ" in await rick()
