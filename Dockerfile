FROM python:3.9-alpine

# Copy
WORKDIR /app
COPY rsserpent rsserpent
COPY requirements.txt ./

# Dependencies
RUN pip install -r requirements.txt && \
    pip install uvicorn && \
    pip cache purge

# Run
EXPOSE 8000
CMD [ "uvicorn", "rsserpent:app", "--host", "0.0.0.0" ]
