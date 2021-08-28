from .builtin import plugin as builtin_plugin
from .externals import plugins as external_plugins


plugins = [builtin_plugin, *external_plugins]

__all__ = ("plugins",)
