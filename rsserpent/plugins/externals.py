from typing import cast

from importlib_metadata import entry_points

from ..models import Plugin


plugins = [cast(Plugin, ep.load()) for ep in entry_points(group="rsserpent.plugin")]

__all__ = ("plugins",)
