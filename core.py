import contextlib

from fastapi import FastAPI


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
