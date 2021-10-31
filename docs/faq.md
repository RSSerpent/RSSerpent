# F.A.Q.

Q: The name of the projcet?

A: This project aims to become a free and open-source alternative to RSSHub, creating RSS feeds for websites that doesn’t provide any. So we want a name like “RSS-something”. Given that this project is to be written in the Python programming language, the word “Serpent” seems more than fit, hence the name – RSSerpent!

---

Q: Why use Python? Why not TypeScript / JavaScript / Go etc?

A: Reasons listed as follows：

I like Python.
RSSerpent is intrinsically a web scraper, for which Python’s rich ecosystem could be an edge.
It is easy to script a small web service in Python.
I loathe JavaScript & Go, TypeScript is mildly acceptable.

---

Q: Is RSSerpent a copycat of RSSHub?

A: I shall answer this question from two aspects:

Idea? Yes. From the RSS-Bridge project that was founded in 2013, to the RSSHub project that was founded in 2018, I could never come up with the idea without these brilliant predecessors.
Implementation? Mostly no. RSSerpent is written in Python, thus destined to be greatly different from RSSHub (written in JavaScript). But as a contributor to RSSHub, I will inevitably refer to parts of its implementation. In fact, RSSerpent was created to solve some issues I saw in RSSHub in the first place.
I will specifically acknowledge RSSHub in the README. Given that RSSHub is open-sourced under the MIT license, I believe these would suffice.

---

Q: With the existing popular RSSHub project, why bother writing another one (RSSerpent)?

A: As mentioned above, RSSerpent was created to solve some issues I saw in RSSHub in the first place. Specifically, these issues are:

Unreasonable mechanism for managing routers (see link). Currently RSSHub adopts a monorepo structure, with all routers residing in the /lib/routes folder. Many contributors come to RSSHub, submit a new router, and maybe never come back again. Therefore, it becomes the responsibility of a few core developers to maintain these routers. Everyday requests for new routers come in and old routers outdate, leading to numerous issues & pull requests that are exhausting to handle. These router-related issues have overwhelmingly outnumbered core-related issues, making it exceedingly difficult to push any advancements on RSSHub core functionalities.
Loss of active developers & maintainers. Currently, the creator of RSSHub, DIYgod, has gone abroad for further study, with his focus shifted to the new RSS3 project. Another maintainer, NeverBehave, struggles to keep the project together. Little helpful active contributors are present and issues are accumulating. Also, the unreasonable routers mechanism could be depleting the passion of developers (repeated, chore, trivial, tedious work).
No type check. RSSHub was initially written in JavaScript, which is a flexible dynamically-typed programming language. However, this flexibility has caused issues for the project’s long-term maintenance. Although there is already a proposal to rewrite RSSHub core in TypeScript, but advancements seem difficult to make.
No proper version control & release schedule (see link). Currently there is no proper release schedule in RSSHub. All users just directly use the code on the master branch. If something went seriously wrong on the master branch, all self-hosted instances could shutdown (e.g. f09b8c4).
Other inevitable issues: after quite some time, parts of the codes have become complex, unreadable, and hard to maintain. These codes become the major obstruction towards debugging, refactoring, and implementing new features.
Please note that these issues are not the fault of RSSHub maintainers. I pay tribute to them in the highest possible manner for maintaining this wonderful open-source software. However, I believe RSSerpent could be a beneficial attempt to learn from RSSHub’s defects and solve these existing issues.

---

Q: What is your overall design of RSSerpent?

A: RSSerpent is an alternative to RSSHub, providing mostly similar functionalities. However, some new mechanisms are to be introduced for solving issues in RSSHub.

Plugins. Routers are no longer mandatory parts of RSSerpent core. Instead, routers are now plugins installed as demanded. Every plugin is an independent python package, loaded into the core by setuptools entry points (link). When installing RSSerpent, users may choose to install plugins of their needs – these plugins might be distributed from PyPI, or simply installed from some git repositories. RSSerpent will officially maintain some popular plugins.
Type check. The RSSerpent project uses python type hints, and performs rigorous type checking with mypy.
Coding conventions. We use black & isort for unifying coding styles, as well as flake8 (and its many plugins) for static analysis: comments, docstrings, naming, functions, complexity are all checked.
Test coverage. We use hypothesis for property-based tests, and we try hard for 100% test coverage.
Release. In RSSerpent core, we release alpha versions with a relatively high frequency (every 5 commit / every 3 day), succeeded by beta versions and stable versions . We want to ensure that every stable release is, like its name, stable and backward compatible. Moreover, the plugin mechanism has brought benefits: plugins can be released/updated at an independent pace, as they are decoupled from the core. You may choose a more radical release/update strategy, if the plugin is expected to frequently change.
Toolchain. RSSerpent core provides common utility functions for processing timezones, lazy-loading, HTML tags etc. We also introduce a plugin template so that developers could use cookiecutter to quickly scaffold & publish a new plugin.
Anti-anti-bot. As part of the toolchain, we’d like to introduce something new so as to improve RSSerpent’s anti-anti-bot capability. Currently we have these ideas in mind: HTTP header auto-generation, caching, rate limiting, proxy pool etc.
Better documentation. We also would like to introduce a series of thorough tutorials & documents to improve developer experience and lower the barriers for beginners. Ideally, a person with basic Python programming skills should be able to write his/her own plugin. Also for international users, we have observed (link1, link2) common complaints about rough onboarding experience, so we are also working on better i18N.
Bounty. RSSHub uses IssueHunt, so that contributors could be rewarded for solving issues. However, very little RSSHub users post issues on IssueHunt. We believe it would be beneficial for RSSerpent to enforce a dedicated platform for requests of new routers, so that developers could be funded for creating new plugins, and people with less programming skills could also get the plugin they want in shorter time!

---

Q: What is the current status of RSSerpent? Is there any short-term plan or roadmap?

A: Currently we have finished Stage 1, released version 0.1.0 (PyPI). Point 1-5, as mentioned above, were mostly completed. In Stage 2, we will focus on point 6-8. In Stage 3, we will finish point 9, create more official plugins, support Atom / JSON feed, and support reading in browser through XSL. The detailed plans of each stage will be released in a kanban.
