FROM python:3.9-alpine

# Setup
RUN addgroup -S app && adduser -S app -G app
RUN apk add --no-cache curl gcc libc-dev libxslt libxslt-dev
USER app

# Copy
WORKDIR /app
COPY --chown=app:app rsserpent rsserpent
COPY --chown=app:app poetry.lock pyproject.toml .

# Dependencies
ENV HOME=/home/app
ENV PATH="${HOME}/.local/bin:${HOME}/.poetry/bin:${PATH}"
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN poetry config virtualenvs.create false && \
    poetry add --lock uvicorn && \
    poetry install --no-dev

# Cleanup
USER root
RUN apk del --no-cache curl gcc libc-dev libxslt-dev
RUN yes | poetry cache clear --all .
USER app

# Run
EXPOSE 8000
CMD [ "uvicorn", "rsserpent:app", "--host", "0.0.0.0" ]
