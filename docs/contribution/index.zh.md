# 环境

无论你是想向 RSSerpent [核心](https://github.com/RSSerpent/RSSerpent)、或是任一 RSSerpent 官方/社区[插件](../plugin/index.md)做贡献，你都需要阅读并依从本文档的指示，来搭建一个开发环境。

## Python

![compatible python versions](https://img.shields.io/pypi/pyversions/rsserpent)

RSSerpent 使用 [Python](https://www.python.org) 编程语言编写。因此，你需要在你的系统上安装 Python 才能运行 RSSerpent。最通用的 Python 安装方式就是到 Python 官方[下载页面](https://www.python.org/downloads/)去下载一个安装包。当然，你也可以通过包管理器来安装：

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
    如果你需要在系统上安装多个 Python 版本，请考虑使用 [pyenv](https://github.com/pyenv/pyenv)。

!!!note
    如果你使用 Windows 系统，你还需要设置环境变量 `PYTHONIOENCODING=utf8`。

!!!warning
    目前 RSSerpent **尚不**支持 Python 3.10。

成功安装以后，你需要运行 `python -V`（或者 `python3 -V`）来确认 Python 的版本。这是因为有些包管理器默认安装的 Python 版本不一定受 RSSerpent 支持。如遇此种情况，请参考包管理器的相关文档来安装受 RSSerpent 支持的 Python 版本。

!!!note
    请确保你的系统上也安装了 [git](https://git-scm.com/)。

## Poetry

[Poetry](https://python-poetry.org/) 是一个现代化的 Python 打包和依赖管理工具，RSSerpent 目前使用 Poetry 来管理项目依赖。请使用如下命令安装 Poetry：

=== "Unix"
    ```bash
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
    ```

=== "Windows"
    ```bash
    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
    ```

## 接下来…

- 如果你想要向 RSSerpent 核心、或者任一已有的 RSSerpent 插件做贡献，请参考[核心](core.md)；
- 如果你想要新建一个 RSSerpent 插件项目，请参考[插件](./plugin/index.md)；
- 如果你想在经济上支持 RSSerpent 项目，请移步 [Open Collective](https://opencollective.com/rsserpent) 或[爱发电](https://afdian.net/@rsserpent)。
