from importlib_metadata import entry_points

from fastapi import FastAPI


app = FastAPI()

for plugin in entry_points(group="rsserpent.plugins"):
    app.include_router(plugin.load())
