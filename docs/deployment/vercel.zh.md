# 使用 Vercel 部署

本教程将帮助你学会如何使用 [Vercel](https://vercel.com) 免费自建 RSSerpent 实例。

## 使用模板

在 GitHub 上打开 RSSerpent Vercel 部署[模板](https://github.com/RSSerpent/rsserpent-deploy-vercel)，然后点击 [![Template Button](https://cdn.jsdelivr.net/gh/rsserpent/asset@latest/template-button.png)](https://github.com/RSSerpent/rsserpent-deploy-vercel/generate) 按钮使用模板。GitHub 会提示你填写一些信息，然后就会基于模板为你创建一个代码仓库。

## 部署项目

在浏览器中打开此[链接](https://vercel.com/new)，选择 *Continue with GitHub*。Vercel 会提示你授权使用你的 GitHub 账户登陆 Vercel。登录成功后，Vercel 会指引你导入 GitHub 代码仓库进行部署。你需要找到你刚刚创建的、名为 `rsserpent-deploy-vercel` 的代码仓库，并点击其右侧的 ![Vercel Import Repository Button](https://cdn.jsdelivr.net/gh/rsserpent/asset@latest/vercel-import-repo-button.png) 按钮。

现在，Vercel 会提示你对项目进行配置。不过好消息是，你完全不需要任何配置！点击 *Deploy*，等待数分钟，你的 RSSerpent 实例就会被成功部署。

## 成功运行 🎉

如果你见到如下界面，那么恭喜你，你已经部署成功了！点击页面中间的网站缩略图，即可在浏览器中打开你的 RSSerpent 实例。

![Vercel Deploy Success](https://cdn.jsdelivr.net/gh/rsserpent/asset@latest/vercel-deploy-success.png)

## 其他事项

如果你需要新增 RSSerpent 插件，请阅读[[安装插件]](plugin.md)。

如果你需要自定义域名，请阅读 Vercel [文档](https://vercel.com/docs/concepts/projects/custom-domains)。
