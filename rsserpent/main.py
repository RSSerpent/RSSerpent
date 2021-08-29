from typing import Any, Dict

import arrow
from flask import Flask, render_template, request
from werkzeug.wrappers import Response

from .models import Feed
from .models.plugin import ProviderFn
from .plugins import plugins
from .utils import fetch_data


app = Flask(__name__)
app.jinja_env.autoescape = True
app.jinja_env.globals["arrow"] = arrow


@app.get("/")
def index() -> str:
    """Return the index HTML web page."""
    return render_template("index.html.jinja")


for plugin in plugins:
    for path, provider in plugin.routers.items():

        def endpoint(
            provider: ProviderFn = provider, **view_args: Dict[str, Any]
        ) -> Response:
            """Return an RSS feed of XML format."""
            data = fetch_data(provider, view_args, dict(request.args))
            content = render_template("rss.xml.jinja", data=Feed(**data), plugin=plugin)
            return Response(content, mimetype="application/xml")

        app.add_url_rule(path, endpoint=path)
        app.view_functions[path] = endpoint
