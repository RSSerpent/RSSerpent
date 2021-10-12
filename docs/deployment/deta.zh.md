# 使用 Deta 部署

本教程将帮助你学会如何使用 [deta.sh](https://www.deta.sh/) 免费自建 RSSerpent 实例。

## 访问令牌

你首先需要注册 Deta 账户才能进行部署，浏览器打开 <https://web.deta.sh> 进行注册。

成功注册并登录后，你需要创建一个 Deta **访问令牌**（access token），然后 RSSerpent 会帮助你完成剩下的事。

1. 打开你的个人主页 `https://web.deta.sh/home/{username}/`；
2. 点击 *Settings* 设置标签页，然后点击 *Create Token* 按钮创建令牌；
3. 将生成的访问令牌拷贝到你的剪贴板。

如果你对访问令牌有任何疑虑，请阅读 Deta 的[文档](https://docs.deta.sh/docs/cli/auth)。

## 使用模板

RSSerpent 为用户提供了 Deta 部署模板，你可以用模板快速完成部署。假设你已经开通 [GitHub](https://github.com/) 账户：

1. 在 GitHub 上打开[模板](https://github.com/RSSerpent/rsserpent-deploy-deta)；
2. 点击绿色的 *Use this template* 按钮使用模板。

GitHub 会提示你填写一些信息，然后就会基于模板为你创建一个代码仓库。

1. 打开你仓库的 *Settings* 设置标签页；
2. 找到 *Secrets*，点击 *New repository secret* 按钮新建密钥;
3. 密钥名字为 *DETA_TOKEN*，密钥内容就是你刚才创建的 Deta 访问令牌.

GitHub 会使用你的访问令牌来将你的 RSSerpent 实例自动部署到 Deta 上。

## 成功运行 🎉

1. 打开你的代码仓库 -> *Actions* 标签页 -> *All workflows* -> *Update*，点击 *Run workflow* 按钮来手动触发第一次部署；
2. 打开你的 Deta 个人主页 -> *default* 项目 -> *Micros*，选择 *rsserpent*，你就能在页面右上角看到你实例的域名（类似 *https://xxxxxx.deta.dev/*）。

在浏览器中打开该域名。如果你看到*“Welcome to RSSerpent!”*这个欢迎信息，那么恭喜你，你已经部署成功了！

## 其他事项

如果你需要新增 RSSerpent 插件，请阅读[安装插件](./plugin.md)。

如果你需要自定义域名，请阅读 Deta [文档](https://docs.deta.sh/docs/micros/custom_domains)。
