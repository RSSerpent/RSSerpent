# 核心

!!!note
    请确保你此前已阅读过[环境](environment.md)。

如果你想要向 RSSerpent 核心（或任一已有的 RSSerpent 插件项目）做贡献，请阅读本教程来学习贡献的整体工作流程。

## 复刻代码

以 RSSerpent [核心](https://github.com/RSSerpent/RSSerpent)为例：

在 GitHub 网站上，找到你想要共享的项目代码仓库。点击页面右上角的 *Fork* 按钮复刻，这样你就能获得一份属于你自己的原代码仓库的复制。

!!!note
    如需进一步了解复刻，请阅读 GitHub [文档](https://docs.github.com/en/get-started/quickstart/fork-a-repo)。

## 安装依赖

将你的复刻代码仓库克隆（clone）到本地。打开终端，使用 `cd` 指令进入仓库目录并运行：

```bash
poetry install
poetry run pre-commit install -t pre-commit -t commit-msg
```

以上命令会为你安装项目依赖和 [pre-commit](https://pre-commit.com/) 钩子。

!!!note
    如需进一步了解克隆，请阅读 GitHub [文档](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)。

    我们推荐你使用 SSH 密钥（而非密码）来连接 GitHub。如需了解如何配置 SSH 密钥，请阅读这篇 GitHub [文档](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)。

## 创建分支

在你的本地代码仓库中，运行 `git checkout -b <分支名>` 以创建一个分支。请在这个分枝上完成你所有的工作，不要去使用 `master`（或 `main`）分支。这样做能保证你的复刻仓库与原仓库之间没有冲突。

一般来说，对于每一个拉去请求，我们都使用不同的分支。取决于你的网络连接质量，安装依赖的过程可能需要数分钟不等。

!!!note
    习惯上，如果你要开发一个新功能，分支名会叫 `feat/xxx`；如果你要修复一个 bug，分支名会叫 `fix/xxx`。

## 拉取请求

在你将本地代码仓库中的变更提交（commit）之后，你需要将这些 commit 推送（push）到远端的 GitHub 仓库里。如果你是第一次在某个分支上进行推送，你需要运行 `git push -u origin <分支名>`；此后你就可以方便地直接运行 `git push`。

完成推送后，打开浏览器，跳转到你复刻的代码仓库。你会在文件列表上方看到一个 *Pull request* 按钮。点击该按钮创建拉取请求。通过拉取请求，你能将你在自己复刻上的工作成果提交到原仓库，而原仓库的维护者会决定是否要接受你的拉取请求。

!!!note
    如需进一步了解拉取请求，请阅读 GitHub [文档](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)。

## 接下来…

到目前为止，我们都在讨论向 RSSerpent 核心做贡献的整体流程。如果你想要找一些具体的问题来解决，你可以：

- 浏览 issue/discussion 列表，找到你感兴趣的内容，在该 issue/discussion 下回复声明你正在解决这个问题，然后尝试提交一个拉取请求。
- 找到一个 bug，创建一个 [issue](https://github.com/RSSerpent/RSSerpent/issues) 说明这个 bug，并尝试提交一个拉取请求解决这个 issue。
- 想出一个新功能，创建一个 [discussion](https://github.com/RSSerpent/RSSerpent/discussions) 说明这个新功能，如果项目维护者愿意接受，你可以尝试提交一个拉取请求来实现这个功能。
