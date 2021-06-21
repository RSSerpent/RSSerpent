from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index() -> str:
    return "Hello World!"
