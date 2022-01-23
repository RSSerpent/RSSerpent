# 获取数据

当你在为你的插件编写数据提供函数时，你需要从某个源网站去获取数据。RSSerpent 提供了一些简单易用的辅助函数，来帮助你在各种场景下获取数据。

## HTTP

从互联网上获取信息的最基本的方式就是使用 HTTP 协议。[HTTPX](https://github.com/encode/httpx/) 是一个强大的异步 Python HTTP 库，且默认被置入 RSSerpent 以便你能直接使用。

有些时候，源网站直接提供了可访问的 JSON API。所以问题就会比较简单：

```python
from rsserpent.utils import HTTPClient


async with HTTPClient() as client:
    response = await client.get("https://httpbin.org/json")
    data = response.json()
```

注意此处 `rsserpent.utils.HTTPClient` 是 `httpx.AsyncClient` 的子类。RSSerpent 扩展出了这个子类，来帮助你在发起 HTTP 请求时自动设置 `Host`、`Referer`、`User-Agent` 等头部信息。

## HTML

还有些时候，源网站不会好心地直接提供 JSON API，所以你需要解析网页的 HTML 源代码来获取数据。[PyQuery](https://pythonhosted.org/pyquery/) 是一个类似 jQuery 的库，它能帮助你从结构化的 HTML 文档中提取数据。PyQuery 也默认被置入 RSSerpent 以便你能直接使用。

```python
from pyquery import PyQuery

from rsserpent.utils import HTTPClient


async with HTTPClient() as client:
    response = await client.get("https://httpbin.org/json")

dom = PyQuery(response.text)
title = dom("h1").text()
description = dom("div > p").text()
```

## 模拟浏览器

在更糟糕的情况下，你需要比 HTTP 协议更强大的武器。许多现代化的网站都大量的使用 JavaScript，因此只有当你在一个真正的、带有 JavaScript 引擎的浏览器环境中打开网页，你才能看到网站的内容被渲染出来。对付这种源网站，你需要使用浏览器模拟。

[Playwright](https://github.com/microsoft/playwright-python) 是一个强大的浏览器自动化框架，且也默认被置入 RSSerpent。RSSerpent 对 playwright 做了一个简单的包装以方便你使用：

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
    浏览器模拟很强大，但也会大量消耗 CPU 和内存资源。所以请仅在必要时小心谨慎地使用浏览器模拟！
