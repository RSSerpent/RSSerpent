from pathlib import Path
from typing import Any, Dict, cast

import arrow
from fastapi import APIRouter, Depends, FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from importlib_metadata import entry_points
from jinja2 import Environment, FileSystemLoader

from .model import Feed, Plugin


app = FastAPI(docs_url=None, redoc_url=None)
templates = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))
templates.globals["arrow"] = arrow


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> str:
    """Define the index endpoint, where an HTML web page is returned."""
    content = templates.get_template("index.html.jinja").render(host=request.base_url)
    return content


for entry_point in entry_points(group="rsserpent.plugins"):
    plugin = cast(Plugin, entry_point.load())
    router = APIRouter()
    for path, provider in plugin.routers.items():

        @router.get(path)
        def endpoint(
            request: Request, data: Dict[str, Any] = Depends(provider)
        ) -> Response:
            """Define a general endpoint for registering plugins."""
            content = templates.get_template("rss.xml.jinja").render(
                data=Feed(**data), plugin=plugin, request=request
            )
            return Response(content=content, media_type="application/xml")

    app.include_router(router)
