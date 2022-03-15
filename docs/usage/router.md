# Routers

Under normal circumstances, every RSS feed has a subscription link. For example, the subscription link of The Guardian World News' feed is [www.theguardian.com/world/rss](https://www.theguardian.com/world/rss). In this subscription link, the part before the first slash `/` is called the *domain* (`www.theguardian.com`), and the other part is called the *route* (`/world/rss`). You can conceive of a subscription link as a virtual pathway, of which the domain is an approximate address while the route is the specific unit/room, etc. The subscription link leads you towards resources you need on the Internet.

!!!note
    The definition of a subscription link here does not necessarily comply with the [URL](https://en.wikipedia.org/wiki/URL) standard. There are simplifications so that readers from a non-tech background can understand more easily.

## Instances and Routes

If you wish to subscribe to news sources without RSS through RSSerpent, you will need to find the subscription link, as usual. RSSerpent's subscription links, similarly, consist of a domain and a route:

- Every domain corresponds to an RSSerpent instance. For example, the official domain [www.rsserpent.com](https://www.rsserpent.com) corresponds to the official instance. You can find more official instances to use on the [[Deploy]](../deploy/index.md) page, but we recommend self-hosting to accommodate your growing and varied requirements.
- By default, an RSSerpent instance contains no route. Maintainers of instances will need to [[Install Plugins]](../deployment/plugin.md) to import routes. If you found a plugin/route missing while using an RSSerpent hosted by others, you can appeal to the instance maintainer or, as recommended, self-host an instance on your own.

!!!note
    An instance is a running copy of the RSSerpent software.

!!!note
    Every RSSerpent plugin contains one or more routes.

RSSerpent's official [instance](https://www.rsserpent.com) comes with the <abbr title="A Chinese video sharing platform akin to Youtube">Bilibili</abbr> [plugin](https://github.com/RSSerpent/rsserpent-plugin-bilibili). Therefore, you can access the `/bilibili/user/{id}/video` route on the official instance to subscribe to some users' published videos. For example, if you wish to subscribe to [Chubbyemu](https://www.youtube.com/channel/UCKOvOaJv4GK-oDqx-sj7VVg)'s official Chinese translation [channel](https://space.bilibili.com/297786973) on Bilibili, you could concatenate the official domain `www.rsserpent.com` and the route `/bilibili/user/297786973/video` to generate the subscription link as follows:

![RSSerpent Bilibili Chubbyemu](https://cdn.jsdelivr.net/gh/rsserpent/asset@latest/rsserpent-bilibili-chubbyemu.png)

## Route Parameters

!!!warning
    Any example under this warning is provided "as is" and does not necessarily work with any instances.

From the example given above, we note that some routes are not complete, and require your information input. Assuming this route can help you subscribe to some users' published videos, the route will need to know *which* users you'd like to subscribe to to work as expected. These information inputs are called *route parameters*.

Route parameters are usually surrounded by brackets `{}`. When filling the route parameters, you should remove the bracket pair. Different routes are provided by different plugins, and you should refer to the documentation of the respective plugin to understand the implication of each route parameter and how you can find and fill in these route parameters.

Again, taking the `/bilibili/user/{id}/video` route for example: the route accepts one route parameter *id*. Every Bilibili user is endowed with a unique ID, which you usually can find in the user profile's address. Only with this unique identifier, the route will then be able to retrieve the user's list of published videos, and output the list in the RSS feed subscription link.

## Query Parameters

Route parameters are required. However, sometimes routes need to access optional or conditional parameters -- we call such parameters *query parameters*:

- Query parameters should be placed after the route, and guarded by a question mark `?`;
- There can be arbitrary amount of query parameters, each looking like `{name}={value}`;
- Multiple query parameters are separated with an ampersand `&`.

For example, assuming the `/bilibili/user/{id}/video` route accepts two query parameters, of which the `sort` parameter is used to specify the sorting criteria while the `order` parameter is used to indicate ascent/descent. Given that most users would probably subscribe to the latest videos, the route by default will sort the list of videos in chronologically descending order. However, if you need to subscribe to the most trending videos, the route should look like `/bilibili/user/{id}/video?sort=hot&order=desc`.
