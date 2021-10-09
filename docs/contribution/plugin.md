# Plugin

## Scaffold

You will need [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html) for quickly scaffolding an RSSerpent plugin, by using the official plugin [template](https://github.com/RSSerpent/template).

```bash
pip install --user cookiecutter
# or on macOS
brew install cookiecutter
# or on Debian/Ubuntu
sudo apt install cookiecutter
```

Now it's time to scaffold you project! In your terminal, start a new session and run:

```bash
cookiecutter gh:rsserpent/template
```

This will download the official RSSerpent plugin [template](https://github.com/RSSerpent/template) from GitHub. You will then be prompted to fill in some information:

```
plugin [rsserpent-plugin-xxx]:
description [An rsserpent plugin for xxx.]:
username [queensferryme]:
link [https://github.com/queensferryme]:
email [queensferryme@example.com]:
```

The message between the brackets `[...]` are default values for respective fields, you may press `Enter` to accept or type in your own choice. You personal information (*email* etc.) will only be used for rendering the template. You could always remain anonymous if you'd like to.

After that, we'll automatically create a directory `rsserpent-plugin-xxx/` with all the necessary project configurations for you. We will also install project dependencies (through `poetry`) and [pre-commit](https://pre-commit.com/) hooks, which may take minutes depending on your network connection.

## Develop

You will need a [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) to start developing. We recommend using [Visual Studio Code](https://code.visualstudio.com/), or VSCode for short. Use VSCode to open the directory you just created using `cookiecutter`. You may be prompted to install some recommended VSCode plugins.

An RSSerpent plugin is mostly a collection of [routers](../usage/router.md), and each router is a `path` string accompanied by a data `provider` function.

```python
from typing import Any, Dict


path = "/path/to/route"


async def provider() -> Dict[str, Any]:
    return {
        "title": "Example",
        "link": "https://example.com",
        "description": "An example rsserpent plugin.",
        "items": [{"title": "Example Title", "description": "Example Description"}],
    }
```

!!!note
    See more example routers [here](https://github.com/RSSerpent/RSSerpent/tree/master/rsserpent/plugins/builtin).

!!!warning
    The `provider` function must be **async** and can **not** have [position-only arguments](https://docs.python.org/3/faq/programming.html#faq-positional-only-arguments).

The `path` variable defines an endpoint where users could access the RSS feed, and the `provider` function provides necessary data for rendering and serving the RSS feed to users. You will also need to register you routers in `rsserpent_plugin_xxx/__init__.py`:

```python
from . import route1, route2, route3


plugin = Plugin(
    # ...
    routers={
        route1.path: route1.provider,
        route2.path: route2.provider,
        route3.path: route3.provider,
    },
)
```

!!!note
    Poetry install dependencies inside a [virtualenv](https://virtualenv.pypa.io/). Therefore, in order to use tools like `pre-commit`, `pytest` or `uvicorn`, you will need to run `poetry shell` or `source $(poetry env info -p)/bin/activate` to activate the virtual environment.

Run `uvicorn --reload rsserpent:app` in your terminal to start an RSSerpent instance locally, so that you can see if you plugin works as expected.

```
➜ uvicorn --reload rsserpent:app
INFO:     Will watch for changes in these directories: ['/path/to/your/directory']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [30920] using statreload
INFO:     Started server process [30922]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

!!!note
    We recommend plugin authors to write tests, so that the plugin can be more robust and have less bugs. Write your tests in the `tests/` directory and run `pytest` to run the tests.

## Publish

After you made enough changes to the plugin locally, make sure to commit your changes and push to GitHub. In this way, you can make you latest work available to plugin users.

```bash
git add --all
git commit -m "<type>: <description>"
git push origin
```

!!!note
    Commit messages should be in accordance with the [Conventional Commits](https://www.conventionalcommits.org/) specification.

When you run `git commit`, a set of `pre-commit` hooks will be triggered. Make sure you pass the checks before actually pushing to GitHub. You could also run the checks manually:

```
➜ pre-commit run --all-files
Nitpick Check............................................................Passed
Fix End of Files.........................................................Passed
Trim Trailing Whitespace.................................................Passed
Check Blanket "#noqa"....................................................Passed
Check Blanket "#type:ignore".............................................Passed
Upgrade Python Syntax....................................................Passed
Check Typos..............................................................Passed
Format Source Code.......................................................Passed
Sort Imports.............................................................Passed
Type Check...............................................................Passed
Lint.....................................................................Passed
```

!!!note
    In `pre-commit` hooks we run [black](https://github.com/psf/black), [isort](https://github.com/pycqa/isort) for source code formatting, [mypy](https://github.com/python/mypy) for type checking, and [flake8](https://github.com/PyCQA/flake8) for linting.
    We also run [**nitpick**](https://github.com/andreoliwa/nitpick), which contains a set of recommended [configurations](https://github.com/RSSerpent/RSSerpent/blob/master/styles/main.toml) for black/isort/mypy/flake8 etc from the upstream.

!!!warning
    If no pre-commit hooks are triggered (that's to say, you didn't lines of checks marked with either *Passed* or *Failed*, as shown above) when you do `git commit`, you can manually install the pre-commit hooks with `pre-commit install -t pre-commit -t commit-msg`.
