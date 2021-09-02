FROM python:3.6-buster
WORKDIR /app
RUN useradd -mU RSSerpent
RUN pip install poetry
RUN apt-get update \
    && apt-get install -y --no-install-recommends gosu \
    && rm -rf /var/lib/apt/lists/
COPY . .
RUN poetry config virtualenvs.create false && poetry install
COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]
EXPOSE 8000
CMD ["poetry","run","uvicorn","rsserpent.main:app","--app-dir","./rsserpent","--host","0.0.0.0"]
