# CHANGELOG

## Unreleased

### BREAKING CHANGES ⚠️

- Drop Python 3.6 and support Python 3.10

### Bug Fixes 🐛

- `CacheKey` is now typed (`3` -> `(3, int)`, `3.0` -> `(3.0, float)`) and positional/keyword arguments are guarded by a sentinel `object()` (#74)

### Documentation 📖

- Contribution guides, for contributing to the RSSerpent core or creating a RSSerpent plugin
- Deployment guides, for self-hosting RSSerpent instances on [Deta](https://www.deta.sh/) and [Heroku](https://www.heroku.com/)

### Features 🎉

- Multi-platform Docker build, for `linux/amd64` and `linux/arm64`
- Replace `pyppeteer` with `playwright` (#76)

## 0.1.4

### Features 🎉

- RSSerpent now builds docker images! Check out [Docker Hub](https://hub.docker.com/r/queensferry/rsserpent/) & [GitHub Container Registry](https://github.com/RSSerpent/RSSerpent/pkgs/container/rsserpent)
- RSSerpent core has made a set of recommended best practices for writing plugins available to plugin authors through [`nitpick`](https://github.com/andreoliwa/nitpick)
- RSSerpent ships some builtin tools for writing plugins, based on [`httpx`](https://github.com/encode/httpx), [`pyquery`](https://github.com/gawel/pyquery), and [`pyppeteer`](https://github.com/pyppeteer/pyppeteer)
    ```python
    from rsserpent.utils import Browser, HTTPClient

    # browser emulation - for sites with javascript
    async with Browser() as browser:
        await browser.goto("https://httpbin.org/html")
        content = await browser.content()

    # send plain HTTP requests with httpx
    async with HTTPClient() as client:
        response = await client.get("https://httpbin.org/get")
        data = response.json()
    ```

## 0.1.3

### BREAKING CHANGES ⚠️

- The `setuptools` entry point for plugin is renamed from `"rsserpent.plugins"` to `"rsserpent.plugin"`
- RSSerpent is refactored, by replacing `fastapi` with `starlette`

### Features 🎉

- Utility functions in `rsserpent.utils` for fighting anti-bot policies, including `@cached` and `@ratelimit`
- RSSerpent will capture exceptions globally and display them as HTML web pages, which could help users and developers of RSSerpent pin down the source of issues

## 0.1.2

### Documentation 📖

- Setup document structure, but contents are left empty for now

## 0.1.1

### Documentation 📖

- Set up documentation, with `mkdocs` and `mkdocs-material`

## 0.1.0

### Features 🎉

- Basic plugin loading functionality, through `setuptools` entry points
- RSS 2.0 feed output, with `pydantic` for modeling and `Jinja2` for templating
