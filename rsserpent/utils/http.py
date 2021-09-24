from typing import Any

import httpx
from fake_useragent import UserAgent  # type: ignore[import]


ua = UserAgent()


class HTTPClient(httpx.AsyncClient):
    """Wrap `httpx.AsyncClient` with default headers."""

    def build_request(self, *args: Any, **kwds: Any) -> httpx.Request:
        """Set default Host/Referer/User-Agent for requests."""
        request = super().build_request(*args, **kwds)
        url = request.url
        request.headers.setdefault("host", url.host)
        request.headers.setdefault("referer", f"{url.scheme}://{url.host}")
        request.headers.setdefault("user-agent", ua.random)
        return request
