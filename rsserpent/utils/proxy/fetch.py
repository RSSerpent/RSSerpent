from typing import AsyncIterator, Dict, Tuple

import httpx
from lxml import html

from rsserpent.models import Proxy


class BaseFetcher:
    """Base class for a proxy fetcher.

    Fetch free http/https proxies from various websites.
    """

    domain: str
    selectors: Dict[str, str]

    @classmethod
    async def elements(  # type: ignore[no-any-unimported]
        cls, limit: int = 10
    ) -> AsyncIterator[Tuple[html.HtmlElement, ...]]:
        """Get elements containing proxy information with CSS selectors.

        Args:
            limit: The maximum number of elements returned.

        Yields:
            a asynchronous generator, each item of which is a tuple of HTML elements.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(cls.domain)
        dom = html.fromstring(response.text)
        for index, elements in enumerate(
            zip(*(dom.cssselect(selector) for selector in cls.selectors.values()))
        ):
            if index == limit:
                break
            yield elements


class FreeProxyListNetFetcher(BaseFetcher):
    """Proxy fetcher for free-proxy-list.net."""

    domain = "https://free-proxy-list.net/"
    selectors = {
        "anonymity": "table.table-striped > tbody > tr > td:nth-child(5)",
        "country": "table.table-striped > tbody > tr > td:nth-child(3)",
        "ip": "table.table-striped > tbody > tr > td:nth-child(1)",
        "port": "table.table-striped > tbody > tr > td:nth-child(2)",
        "proto": "table.table-striped > tbody > tr > td:nth-child(7)",
    }

    @classmethod
    async def fetch(cls) -> AsyncIterator[Proxy]:
        """Fetch proxies from <https://free-proxy-list.net/>."""
        async for elements in cls.elements():
            anonymity, country, ip, port, proto = elements
            yield Proxy(
                anonymity=anonymity.text_content().split()[0],
                country=country.text_content(),
                ip=ip.text_content(),
                port=port.text_content(),
                proto="https" if proto.text_content() == "yes" else "http",
            )


class SSLProxiesOrgFetcher(FreeProxyListNetFetcher):
    """Proxy fetcher for sslproxies.org."""

    domain = "https://sslproxies.org/"

    @classmethod
    async def fetch(cls) -> AsyncIterator[Proxy]:
        """Fetch proxies from <https://sslproxies.org/>."""
        async for proxy in super().fetch():
            yield proxy
