# Know about RSS

!!!note
    Before learning to use RSSerpent, you should have a basic understanding of RSS itself. Proceed to the next chapter if you already understood.

## What is RSS?

[RSS](https://en.wikipedia.org/wiki/RSS), short for Really Simple Syndication, is a web feed format. Other common web feed formats include [Atom](https://en.wikipedia.org/wiki/Atom_(Web_standard)), [JSON Feed](https://en.wikipedia.org/wiki/JSON_Feed), etc. As the oldest and most popular web feed format, RSS is also often used as the collective name of RSS, Atom, and other web feed formats.

As a web feed format, RSS is capable of pushing some frequently updated content to end-users over the Internet. One typical application of RSS is in the *news* industry. To this day, many news publishers, including BBC News, The Guardian, etc, still provide RSS news subscriptions.

## Why use RSS?

RSS is most convenient for content readers. By subscribing to RSS feeds, you could aggregate information from various sources into one united place, thus eliminating the need to open multiple tabs/applications to skim through. What's even better, you can filter and prioritize based on the then aggregated information, in order to retrieve the most valuable pieces and save your precious reading time. Many RSS feeds also provide full-text output (instead of abstraction), so that you don't even have to open the browser to read the article. You will be free of cookie tracking, and your privacy will be preserved.

However, RSS is not as friendly to content publishers. Because RSS does not require you to open a browser or accept tedious cookie policies, it will be increasingly difficult for content publishers to profit from advertisement and personal data. As a result, fewer and fewer content publishers provide RSS subscriptions nowadays. RSSerpent would like to change this situation, so that content readers can benefit from more independent, convenient, and free access to the information on the Internet.

## How to use RSS?

Usually, you subscribe to an RSS feed with a link (URL). RSS subscription links, by default, generate data in formats (e.g. XML, JSON) that are easier for computers to process and exchange. Therefore, we will also need an RSS reader to convert the RSS feed format into a more human-readable format.

Taking the RSS subscription [link](https://www.theguardian.com/world/rss) of The Guardian's World News as an example:

![The Guardian feed](https://cdn.jsdelivr.net/gh/rsserpent/asset/the-guardian-feed.png)

By opening that subscription link in the browser, you are likely to be confronted with this incomprehensible document. Don't panic! You are not mandated to understand anything about computer programming in order to learn about how to use RSS 😉 The only thing you will need to know is the link in the browser's address bar. Copy that subscription link to your clipboard, open your RSS reader, paste that link, and you will successfully subscribe to the RSS feed.

There are plenty of RSS readers available out there. You can find many of them simply through the search engine. The [All about RSS](https://github.com/AboutRSS/ALL-about-RSS#-rss-readers) repository also exhibits a fine collection of popular RSS readers for your reference. Here is a list of options recommended by the RSSerpent document:

- `#General` [Feedly](https://feedly.com/)，[Inoreader](https://www.inoreader.com/)
- `#Apple` [NetNewsWire](https://netnewswire.com/)，[Reeder](https://reederapp.com/)
- `#Android` [FeedMe](https://play.google.com/store/apps/details?id=com.seazon.feedme)

!!!note
    RSSerpent itself is not an RSS reader. RSSerpent is used for creating RSS feeds.
