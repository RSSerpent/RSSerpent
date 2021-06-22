from importlib_metadata import entry_points

from fastapi import Depends, FastAPI


app = FastAPI()

for plugin in entry_points(group="rsserpent.plugins"):
    path, provider = plugin.load()
    # register the plugin at `path`
    @app.get(path)
    def router(data: dict = Depends(provider)) -> dict:
        return data
