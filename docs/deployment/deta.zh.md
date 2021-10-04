# 使用 Deta.sh 部署

本教程将帮助你学会如何使用 [deta.sh](https://www.deta.sh/) 免费自建 RSSerpent 实例。

## 注册

你首先需要注册 [deta.sh](https://www.deta.sh/) 账户才能进行部署：

1. 打开 <https://web.deta.sh> 并注册；
2. 填写*用户名*，*密码*和*邮箱地址*；
3. 打开邮箱，点击确认邮件。

如果你已有账户，跳过这一步直接登录即可。

## 访问令牌

你需要创建一个 [deta.sh](https://www.deta.sh/) 访问令牌（access token），然后 RSSerpent 会帮助你完成剩下的事。

1. 打开你的个人主页 `https://web.deta.sh/home/{username}/`；
2. 点击 *Settings* 设置标签页，然后点击 *Create Token* 按钮创建令牌；
3. 将生成的访问令牌拷贝到你的剪贴板。

如果你对访问令牌有任何疑虑，请阅读 Deta 的[文档](https://docs.deta.sh/docs/cli/auth)。

## 使用模板

RSSerpent 为用户提供了 [deta.sh](https://www.deta.sh/) 部署模板，你可以用模板快速完成部署。假设你已经开通 [GitHub](https://github.com/) 账户：

1. 在 GitHub 上打开[模板](https://github.com/RSSerpent/rsserpent-deploy-deta)；
2. 点击绿色的 *Use this template* 按钮使用模板。

GitHub 会提示你一些信息，然后就会（基于模板）为你创建一个代码仓库。

1. 打开你仓库的 *Settings* 设置标签页；
2. 找到 *Secrets*，点击 *New repository secret* 按钮新建密钥;
3. 密钥名字为 *DETA_TOKEN*，密钥内容就是你刚才创建的 [deta.sh](https://www.deta.sh/) 访问令牌.

GitHub 会使用你的访问令牌来自动将你的 RSSerpent 实例部署到 [deta.sh](https://www.deta.sh/) 上。

## 添加插件

默认的模板功能并不丰富，你需要将添加你需要的 RSSerpent 插件到 `rsserpent.txt` 文件中。你可以使用 `git` 将仓库克隆本地进行编辑，或者你也可以使用 GitHub 网页进行编辑。

编写 `rsserpent.txt` 时的一些注意事项：

- 编写 `rsserpent.txt` 和为任何 Python 项目编写 `requirements.txt` 是一样的；
- 不要修改 `requirements.txt`，你只应该修改 `rsserpent.txt`。GitHub Actions 会负责自动更新你的 `requirements.txt` 并部署实例；
- 每周一次，或者每次你修改仓库内容并提交时，会进行自动更新/部署；
- 我们推荐你在 `rsserpent.txt` 中不要指定依赖项的版本，这样 [GitHub Actions](https://github.com/features/actions) 能帮助你自动将依赖更新到最新版；

```
# PyPI
rsserpent
# Git
rsserpent-plugin-bilibili @ git+https://github.com/RSSerpent/rsserpent-plugin-bilibili.git
```
- 如果你确认你需要使用某个特定版本（而非最新）的依赖，你可以：

```
# PyPI
rsserpent==0.1.4
# Git
rsserpent-plugin-bilibili @ git+https://github.com/RSSerpent/rsserpent-plugin-bilibili.git@0609c0bd466e5d19fbb13078d9b93e0134b8c5bd
```

## 成功运行 🎉

1. 打开你的代码仓库 --> *Actions* 标签页 --> *Update*，点击 *Run workflow* 按钮来手动触发一次部署；
2. 打开你的 [deta.sh](https://www.deta.sh/) 个人主页 --> *default* 项目 --> *Micros* 标签页，选择 *rsserpent*，你就能在页面右上角看到你实例的域名（类似 *https://xxxxxx.deta.dev/*）。

在浏览器中打开该域名。如果你看到“Welcome to RSSerpent!”这个欢迎信息，那么恭喜你，你已经部署成功了！
