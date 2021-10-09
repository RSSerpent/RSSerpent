# 插件

## 搭建项目

首先，你需要安装 [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)，以便能使用官方插件[模板](https://github.com/RSSerpent/template)来快速搭建一个 RSSerpent 插件项目。

```bash
pip install --user cookiecutter
# or on macOS
brew install cookiecutter
# or on Debian/Ubuntu
sudo apt install cookiecutter
```

现在可以开始搭建项目了！在你的终端里，打开一个新的会话页面并执行：

```bash
cookiecutter gh:rsserpent/template
```

这个命令首先会从 GitHub 下载 RSSerpent 官方插件模板，随后会提示你填写一些信息（从上往下依次是插件名、插件描述、作者名、作者主页链接、作者邮箱）：

```
plugin [rsserpent-plugin-xxx]:
description [An rsserpent plugin for xxx.]:
username [queensferryme]:
link [https://github.com/queensferryme]:
email [queensferryme@example.com]:
```

方括号 `[...]` 之间的文本时对应字段的默认值，你可以按下回车键接受默认值，也可以自己在冒号后输入内容。你的个人信息（*邮箱地址*等）只会被用来填充项目模板，你也可以选择不填写并保持匿名。

填写完成后，我们会为你自动创建一个名为 `rsserpent-plugin-xxx/` 的文件夹，里面包含了所有基本项目配置。然后还会使用 `poetry` 安装项目依赖，并安装 [pre-commit](https://pre-commit.com/) 钩子 —— 取决于你的网络连接质量，这一步可能需要数分钟不等。

## 进行开发

我们推荐你使用 [Visual Studio Code](https://code.visualstudio.com/)（简称 VSCode）这一集成开发环境（IDE）进行插件开发。使用 VSCode 打开你刚刚创建的文件夹，VSCode 可能会提示你安装一些推荐的 VSCode 插件。安装完成后，你就可以开始开发 RSSerpent 插件了。

RSSerpent 插件的主要部分就是一系列[路由](../usage/router.md)，每个路由都包含一个 `path` 字符串和一个数据提供函数 `provider`。

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
    你可以在[这里](https://github.com/RSSerpent/RSSerpent/tree/master/rsserpent/plugins/builtin)找到更多路由范例。

!!!warning
    数据提供函数 `provider` 必须是 **async** 函数，并且不能包含 [position-only arguments](https://docs.python.org/3/faq/programming.html#faq-positional-only-arguments)。


字符串 `path` 定义了一个路径，用户可以从这个路径来访问到 RSS 订阅链接；数据提供函数 `provider` 则负责提供相应的数据，这些数据会被用于创建可订阅的 RSS 内容并呈现给用户。作为插件开发者，你还需要将路由注册到 `rsserpent_plugin_xxx/__init__.py`：

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
    Poetry 将你的项目依赖安装在一个隔离的[虚拟环境](https://virtualenv.pypa.io/)中。因此，你需要使用 `poetry shell` 或 `source $(poetry env info -p)/bin/activate` 命令来激活虚拟环境，才可以使用虚拟环境中的 `pre-commit`，`pytest`，`uvicorn` 等命令行工具。

在终端里执行 `uvicorn --reload rsserpent:app`，你就能在本地启动一个 RSSerpent 实例。你可以在浏览器中打开这个实例，用以调试你的插件。

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
    强烈推荐插件作者编写测试，以确保你的插件能更鲁棒、没有错误。测试需要编写在 `tests/` 文件夹中，并使用 `pytest` 命令来运行。

## 发布插件

当你在本地对插件进行了足够多的改动后，请确保你讲这些改动提交（commit）并推送（push）到 GitHub。这样子，你插件的用户才能使用到你的最新工作成果。

```bash
git add --all
git commit -m "<type>: <description>"
git push origin
```

!!!note
    提交信息（commit message）应该遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范。

当你运行 `git commit` 提交时，你会自动触发一系列 `pre-commit` 钩子，这些钩子会对你的代码等进行检查。请确保你将改动推送到 GitHub 前已成功通过所有检查。你也可以执行如下命令来手动进行检查：

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
    我们在 `pre-commit` 钩子中运行了 [black](https://github.com/psf/black)/[isort](https://github.com/pycqa/isort) 代码格式化, [mypy](https://github.com/python/mypy) 类型检查，以及 [flake8](https://github.com/PyCQA/flake8) 代码风格检查。
    我们还运行了 [**nitpick**](https://github.com/andreoliwa/nitpick) 这个钩子：它包含了一系列 RSSerpent 官方推荐的 black/isort/mypy/flake8 等开发工具的[配置](https://github.com/RSSerpent/RSSerpent/blob/master/styles/main.toml)，希望插件开发者能够遵守。

!!!warning
    如果你在执行 `git commit` 时，没有触发任何 pre-commit 钩子（也就是说，没有看到如上标记有 *Passed* 通过或 *Failed* 失败的若干行检查），你可以运行 `pre-commit install -t pre-commit -t commit-msg` 来手动安装 pre-commit 钩子。
