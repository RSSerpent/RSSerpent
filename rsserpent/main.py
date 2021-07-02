from pathlib import Path
from typing import cast

import arrow
from fastapi import APIRouter, Depends, FastAPI, Request, Response
from importlib_metadata import entry_points
from jinja2 import Environment, FileSystemLoader

from .model import Feed, Plugin


app = FastAPI()
templates = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))
templates.globals["arrow"] = arrow


for entry_point in entry_points(group="rsserpent.plugins"):
    plugin = cast(Plugin, entry_point.load())
    router = APIRouter()
    for path, provider in plugin.routers.items():

        @router.get(path, summary=provider.__name__, description=provider.__doc__)
        def endpoint(request: Request, data: dict = Depends(provider)) -> Response:
            """Define a general endpoint for registering plugins."""
            content = templates.get_template("rss.xml.jinja").render(
                data=Feed(**data), plugin=plugin, request=request
            )
            return Response(content=content, media_type="application/xml")

    app.include_router(router, tags=[plugin.name])
