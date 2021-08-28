from ...models import Persona, Plugin
from . import example


plugin = Plugin(
    name="rsserpent-plugin-builtin",
    author=Persona(
        name="queensferryme",
        link="https://github.com/queensferryme",
        email="queensferry.me@gmail.com",
    ),
    repository="https://github.com/RSSerpent/RSSerpent",
    prefix="/_",
    routers={example.path: example.provider},
)
