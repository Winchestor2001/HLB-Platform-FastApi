from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from piccolo_admin import create_admin
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from piccolo.engine import engine_finder

from src import APP_CONFIG
from src.routers import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = engine_finder()
    await engine.start_connection_pool()
    try:
        yield
    finally:
        await engine.close_connection_pool()


app = FastAPI(
    title="HLB Platform API",
    version="1.0.0",
    openapi_url="/api/openapi.json",
    default_response_class=UJSONResponse,
    lifespan=lifespan,
    routes=[
        Mount(
            "/admin/",
            create_admin(
                tables=APP_CONFIG
            ),
        ),
        Mount("/static/", StaticFiles(directory="static")),
        Mount("/media/", StaticFiles(directory="media")),
    ],
)

app.include_router(api_router, prefix="/api")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
