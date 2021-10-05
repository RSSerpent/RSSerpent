# 安装插件

!!!warning
    注意不要混淆 **`rsserpent.txt`** 和 `requirements.txt`。

默认的模板功能并不丰富，你需要将添加你需要的 RSSerpent 插件到 `rsserpent.txt` 文件中。你可以使用 [git](https://git-scm.com/) 将仓库克隆到本地以编辑 `rsserpent.txt`，或者也可以使用 GitHub 网页进行编辑。

编写 `rsserpent.txt` 时的一些注意事项：

- 编写 `rsserpent.txt` 和为任何 Python 项目编写 `requirements.txt` 是一样的；
- 不要修改 `requirements.txt`，你只应该修改 `rsserpent.txt`。GitHub Actions 会负责自动更新你的 `requirements.txt` 并部署实例；
- 每周一次，或者每次你修改仓库内容并提交时，会进行自动更新/部署；
- 我们推荐你在 `rsserpent.txt` 中不要指定任何版本，这样 [GitHub Actions](https://github.com/features/actions) 能帮助你自动将依赖更新到最新版；

```python
# PyPI
rsserpent
# Git
rsserpent-plugin-bilibili @ git+https://github.com/RSSerpent/rsserpent-plugin-bilibili.git
```
- 如果你确认你需要使用某个特定版本（而非最新）的依赖，你可以：

```python
# PyPI
rsserpent==0.1.4
# Git
rsserpent-plugin-bilibili @ git+https://github.com/RSSerpent/rsserpent-plugin-bilibili.git@0609c0bd466e5d19fbb13078d9b93e0134b8c5bd
```
