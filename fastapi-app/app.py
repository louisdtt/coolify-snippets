from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def index():
    return "Hello from FastAPI on Coolify!"


@app.get("/health")
def health():
    return {"status": "ok"}
