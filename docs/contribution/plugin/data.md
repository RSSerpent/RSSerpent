# Retrieving Data

When you are writing a data provider function, you need to retrieve data from a source website. RSSerpent ships with convenient utility functions for you to retrieve data in various scenarios.

## HTTP

The most basic, bare-bone way to retrieve data from the Internet is by using the HTTP protocol. [HTTPX](https://github.com/encode/httpx/), a powerful HTTP library for Python with asynchronous API, is bundled with the RSSerpent core.

Sometimes the source website has a directly accessible JSON API, so you can simply:

```python
from rsserpent.utils import HTTPClient


async with HTTPClient() as client:
    response = await client.get("https://httpbin.org/json")
    data = response.json()
```

Here, `rsserpent.utils.HTTPClient` is a subclass of `httpx.AsyncClient`, despite that `HTTPClient` will automatically set `Host`, `Referer`, and `User-Agent` headers for you.

## HTML

The source website is sometimes not kind enough to offer you convenient JSON API, so you have to parse the HTML in order to retrieve data. [PyQuery](https://pythonhosted.org/pyquery/) is here to help -- it lets you retrieve data from HTML documents by using a jQuery-like API, and it is also bundled with RSSerpent!

```python
from pyquery import PyQuery

from rsserpent.utils import HTTPClient


async with HTTPClient() as client:
    response = await client.get("https://httpbin.org/json")

dom = PyQuery(response.text)
title = dom("h1").text()
description = dom("div > p").text()
```

## Browser Emulation

In worse situations, HTTP is simply not enough. Many modern websites are loaded with JavaScript, and the true content of the website won't be rendered unless you are running in a genuine browser environment with a JavaScript engine. In this case, you need a browser emulator.

[Pyppeteer](https://github.com/pyppeteer/pyppeteer) is a powerful browser automation library and it's bundled with RSSerpent. RSSerpent also provides a convenient wrapper on top of pyppeteer:

```python
from pyquery import PyQuery

from rsserpent.utils import Browser


async with Browser() as browser:
    await browser.goto("https://httpbin.org/html")
    content = await browser.content()

dom = PyQuery(content)
title = dom("h1").text()
description = dom("div > p").text()
```

!!!warning
    Browser emulation's power comes with a cost, as it strains CPU & memory resources. Be cautious! Use browser emulation only when necessary.
