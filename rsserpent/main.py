from functools import partial
from pathlib import Path
from typing import cast

import arrow
from fastapi import Depends, FastAPI, Request, Response
from importlib_metadata import entry_points
from jinja2 import Environment, FileSystemLoader

from .model import Feed, Plugin


app = FastAPI()
templates = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))
templates.globals["arrow"] = arrow


# NOTE: I don't know why, but `mypy` refuses to follow imports, resulting
# in that `Request` & `Response` effectively becomes `Any` type. Temporarily
# ignores the next line when performing type checks :(
def endpoint(data: dict, plugin: Plugin, request: Request) -> Response:  # type: ignore
    """Define a general endpoint for registering plugins."""
    content = templates.get_template("rss.xml.jinja").render(
        data=Feed(**data), plugin=plugin, request=request
    )
    return Response(content=content, media_type="application/xml")


for entry_point in entry_points(group="rsserpent.plugins"):
    plugin = cast(Plugin, entry_point.load())
    for path, provider in plugin.routers.items():
        app.add_api_route(
            path,
            partial(endpoint, data=Depends(provider), plugin=plugin),
            methods=["GET"],
        )
