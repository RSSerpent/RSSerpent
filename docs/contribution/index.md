# Environment

Whether you are contributing the RSSerpent [core](https://github.com/RSSerpent/RSSerpent), or any of the official & community RSSerpent [plugins](../plugin/official.md), you need to follow this tutorial to set up a basic development environment.

## Python

![compatible python versions](https://img.shields.io/pypi/pyversions/rsserpent)

RSSerpent is written in the [Python](https://www.python.org) programming language. You must have a valid Python installation on your system in order to get RSSerpent up & run. The most universal way to install Python is to grab a installer from the official Python [download page](https://www.python.org/downloads/). An alternative approach is to install via a package manager:

=== "Linux"
    ```bash
    # Arch
    sudo pacman -S python
    # Debian/Ubuntu
    sudo apt update
    sudo apt install python3 python3-pip
    ```

=== "macOS"
    ```bash
    # Homebrew
    brew install python
    # MacPorts
    sudo port selfupdate
    sudo port install python
    ```

=== "Windows"
    ```bash
    # Chocolatey
    choco install python
    # Scoop
    scoop install python
    ```

!!!note
    If you need to manage multiple versions of Python on your system, checkout [pyenv](https://github.com/pyenv/pyenv).

!!!note
    If you are using Windows, you will need to set the environment variable `PYTHONIOENCODING=utf8`.

!!!warning
    Currently RSSerpent does **not** support Python 3.10.

After successful installation, you need to run `python -V` (or `python3 -V`) to verify the currently installed Python's version, as the default Python version provided by some package managers might not be compatible with RSSerpent. Please refer to the documentation of respective package manager to install a compatible Python version.

!!!note
    Make sure you have [git](https://git-scm.com/) installed too.

## Poetry

[Poetry](https://python-poetry.org/) is a modern Python packaging and dependency management tool and is currently used by RSSerpent. Install `poetry` with:

=== "Unix"
    ```bash
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
    ```

=== "Windows"
    ```bash
    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
    ```

## Further Steps

- If you are contributing to the RSSerpent core, or an existing RSSerpent plugin project, please refer to [Core](core.md);
- If you are starting a new RSSerpent plugin project, please refer to [Plugin](plugin.md);
- If you'd like to financially support the RSSerpent project, check out [Open Collective](https://opencollective.com/rsserpent) or [爱发电](https://afdian.net/@rsserpent).
