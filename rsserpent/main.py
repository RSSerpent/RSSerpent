import arrow
from flask import Flask, render_template, request
from werkzeug.wrappers import Response

from .models import Feed
from .plugins import plugins


app = Flask(__name__)
app.jinja_env.autoescape = True
app.jinja_env.globals["arrow"] = arrow


@app.get("/")
def index() -> str:
    """Return the index HTML web page."""
    return render_template("index.html.jinja")


for plugin in plugins:
    for path, provider in plugin.routers.items():

        def endpoint() -> Response:
            """Return an RSS feed of XML format."""
            data = provider(request.view_args or {}, dict(request.args))
            content = render_template("rss.xml.jinja", data=Feed(**data), plugin=plugin)
            return Response(content, mimetype="application/xml")

        app.add_url_rule(path, endpoint=path)
        app.view_functions[path] = endpoint
