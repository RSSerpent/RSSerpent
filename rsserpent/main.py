from typing import Any, Dict

import arrow
from fastapi import APIRouter, Depends, FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from importlib_metadata import entry_points
from jinja2 import Environment, PackageLoader

from .model import Feed, Plugin


app = FastAPI(docs_url=None, redoc_url=None)
templates = Environment(autoescape=True, loader=PackageLoader("rsserpent"))
templates.globals["arrow"] = arrow


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> str:
    """Return the index HTML web page."""
    content = templates.get_template("index.html.jinja").render(host=request.base_url)
    return content


for entry_point in entry_points(group="rsserpent.plugins"):
    plugin: Plugin = entry_point.load()
    router = APIRouter()
    for path, provider in plugin.routers.items():

        @router.get(path)
        def endpoint(
            request: Request, data: Dict[str, Any] = Depends(provider)  # noqa: B008
        ) -> Response:
            """Returns an RSS feed of XML format.

            Args:
                request: The incoming HTTP request.
                data: The data provided by an external plugin to render the response.

            Returns:
                An HTTP response with mimetype `application/xml`.The content of this
                HTTP response is a subscriptable RSS feed.
            """
            content = templates.get_template("rss.xml.jinja").render(
                data=Feed(**data), plugin=plugin, request=request
            )
            return Response(content=content, media_type="application/xml")

    app.include_router(router)
