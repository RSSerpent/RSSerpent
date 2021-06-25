from typing import cast

from fastapi import Depends, FastAPI
from importlib_metadata import entry_points

from .model.plugin import Plugin


app = FastAPI()

for entry_point in entry_points(group="rsserpent.plugins"):
    plugin = cast(Plugin, entry_point.load())

    for path, provider in plugin.routers.items():

        @app.get(path)
        def router(data: dict = Depends(provider)) -> dict:  # noqa
            return data
