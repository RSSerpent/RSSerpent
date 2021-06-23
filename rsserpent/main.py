from fastapi import Depends, FastAPI
from importlib_metadata import entry_points


app = FastAPI()

for plugin in entry_points(group="rsserpent.plugins"):
    path, provider = plugin.load()

    @app.get(path)
    def router(data: dict = Depends(provider)) -> dict:  # noqa
        return data
