# 认识 RSS

!!!note
    在使用 RSSerpent 前，你首先需要对 RSS 有足够的认知。如果你相信自己已经做到了这一点，可以跳过本章节。

## 什么是 RSS

[RSS](https://en.wikipedia.org/wiki/RSS) 是 Really Simple Syndication 的缩写，中文译作“简易信息聚合”。RSS 是一种互联网消息来源的格式。其他常见的消息来源格式还包括 [Atom](https://en.wikipedia.org/wiki/Atom_(Web_standard))、[JSON Feed](https://en.wikipedia.org/wiki/JSON_Feed) 等。作为最早出现也最流行的消息来源格式，RSS 也常被用作 RSS、Atom 等消息来源格式的统称。

作为一种消息来源的格式，RSS 能够向用户推送网络上一些频繁更新的内容 —— 其中的一个典型应用就是*新闻*。时至今日，许多新闻发布者都仍在通过 RSS 发布新闻，例如 BBC New、The Guardian 等。

## 为什么选择 RSS

RSS 对于内容阅读者来说是方便的。通过订阅 RSS，你可以将多个来源的信息聚合在一处浏览，这样就免去了你在获取信息时不得不打开多个网页/应用逐一查看的麻烦。更棒的是，你还可以在此基础上对聚合信息作过滤、筛选、排序，从中挑选出最有价值的信息，以节省你宝贵的时间。许多 RSS 还会将相关内容全文输出，这样你甚至不必打开网页/应用就能阅读，你得以免于 Cookie 等追踪手段的干扰，你的隐私也安全无虞。

但 RSS 对于内容发布者却并不尽然友好。尤其是在 RSS 免去了阅读者打开网页/应用的麻烦、免去了受 Cookie 追踪隐私的困扰之后，内容发布者的广告收益与其他潜在商机势必要受到损害。于是时至今日，越来越少的内容发布者允许用户通过 RSS 来订阅内容。因此，RSSerpent 项目希望改善这一局面，让更多用户能够通过 RSS 独立、便捷、自由地获取互联网上的信息。

## 如何使用 RSS

通常来说，你可以通过一个链接来订阅 RSS。RSS 订阅链接默认会输出更易于计算机理解的数据交换格式，例如 XML、JSON 等。因此，我们还需要一个 RSS 阅读器，来帮助我们将 RSS 订阅链接中的内容转换为更易于人类阅读的形式。

下面以卫报世界新闻的 RSS 订阅[链接](https://www.theguardian.com/world/rss)在某一时刻输出的内容为例：

![The Guardian feed](https://cdn.jsdelivr.net/gh/rsserpent/asset@latest/the-guardian-feed.png)

在浏览器中打开该订阅链接，你可能会看到这样一份难以理解的 XML 格式文档。请不要惊慌：你无需从事任何计算机编程相关工作就可以学会如何使用 RSS 😉 你需要关注的只有浏览器地址栏中的那个链接 —— 也就是卫报世界新闻的 RSS 订阅链接。将该链接拷贝到剪贴板，然后打开你的 RSS 阅读器，输入该链接，你就可以成功订阅该信息源了。

市面上有大量 RSS 阅读器可供选择，你可以通过搜索引擎来寻找你钟意的阅读器。[All about RSS](https://github.com/AboutRSS/ALL-about-RSS#-rss-readers) 仓库里也收集了不少较为流行的选项，值得作为参考。本文档也将列举若干常见的 RSS 阅读器供读者尝试：

- `#通用` [Feedly](https://feedly.com/)，[Inoreader](https://www.inoreader.com/)
- `#苹果` [NetNewsWire](https://netnewswire.com/)，[Reeder](https://reederapp.com/)
- `#安卓` [FeedMe](https://play.google.com/store/apps/details?id=com.seazon.feedme)

!!!note
    RSSerpent 本身并不是 RSS 阅读器，RSSerpent 用于生成 RSS 订阅链接。
