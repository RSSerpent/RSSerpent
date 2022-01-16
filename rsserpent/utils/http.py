from typing import Any

import httpx
from fake_useragent import UserAgent  # type: ignore[import]
from pyppeteer import launch
from pyppeteer.page import Page


ua = UserAgent(
    fallback="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
)


class Browser:
    """Wrap `pyppeteer.browser.Browser` as a context manager."""

    async def __aenter__(self) -> Page:
        """Enter the context manager."""
        self.browser = await launch(
            handleSIGHUP=False, handleSIGINT=False, handleSIGTERM=False, headless=True
        )
        self.page = await self.browser.newPage()
        return self.page

    async def __aexit__(self, *args: Any) -> None:
        """Leave the context manager."""
        await self.browser.close()


class HTTPClient(httpx.AsyncClient):
    """Wrap `httpx.AsyncClient` with default headers."""

    def build_request(self, *args: Any, **kwds: Any) -> httpx.Request:
        """Set default Host/Referer/User-Agent for requests."""
        request = super().build_request(*args, **kwds)
        url = request.url
        request.headers.setdefault("Host", url.host)
        request.headers.setdefault("Referer", f"{url.scheme}://{url.host}")
        request.headers.setdefault("User-Agent", ua.random)
        return request
