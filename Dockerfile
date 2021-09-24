FROM python:3.9-alpine

# Copy
WORKDIR /app
COPY rsserpent rsserpent
COPY requirements.txt ./
COPY scripts/docker-entrypoint.sh /

# Dependencies
RUN apk add --no-cache gcc libc-dev libxml2-dev libxslt libxslt-dev
RUN pip install -r requirements.txt && \
    pip install uvicorn && \
    pip cache purge
RUN apk del gcc libc-dev libxml2-dev libxslt-dev

# Run
EXPOSE 8000
ENTRYPOINT [ "/docker-entrypoint.sh" ]
CMD [ "uvicorn", "rsserpent:app", "--host", "0.0.0.0" ]
