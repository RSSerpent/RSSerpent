from functools import partial
from pathlib import Path
from typing import Optional, cast

import arrow
from fastapi import Depends, FastAPI, Request, Response
from fastapi.routing import APIRoute
from importlib_metadata import entry_points
from jinja2 import Environment, FileSystemLoader

from .model import Feed, Plugin


templates = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))
templates.globals["arrow"] = arrow


def endpoint(data: dict, plugin: Plugin, request: Request) -> Response:
    """Define a general endpoint for registering plugins."""
    content = templates.get_template("rss.xml.jinja").render(
        data=Feed(**data), plugin=plugin, request=request
    )
    return Response(content=content, media_type="application/xml")


routes = []
for entry_point in entry_points(group="rsserpent.plugins"):
    plugin = cast(Plugin, entry_point.load())
    for path, provider in plugin.routers.items():
        routes.append(
            APIRoute(
                path,
                partial(endpoint, data=Depends(provider), plugin=plugin),
                methods=["GET"],
            )
        )

app = FastAPI(routes=cast(Optional[list], routes))
