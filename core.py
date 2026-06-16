import contextlib

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from template_core import templates


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        yield

    finally:
        pass


app = FastAPI(
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")
