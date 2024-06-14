from contextlib import asynccontextmanager

from fastapi import FastAPI
from piccolo_admin import create_admin
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.staticfiles import StaticFiles
from piccolo.engine import engine_finder

from src import APP_CONFIG


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = engine_finder()
    await engine.start_connection_pool()
    try:
        yield
    finally:
        await engine.close_connection_pool()


app = FastAPI(
    lifespan=lifespan,
    routes=[
        Mount(
            "/admin/",
            create_admin(
                tables=APP_CONFIG,
            ),
        ),
        Mount("/static/", StaticFiles(directory="static")),
        Mount("/media/", StaticFiles(directory="media")),
    ],
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', host="0.0.0.0", port=8000)
