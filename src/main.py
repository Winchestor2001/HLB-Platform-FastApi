from fastapi import FastAPI
from piccolo_admin import create_admin
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.staticfiles import StaticFiles
from src.db.piccolo_app import APP_CONFIG

app = FastAPI(
    routes=[
        Mount(
            "/admin/",
            create_admin(
                tables=APP_CONFIG.table_classes,
                # Required when running under HTTPS:
                # allowed_hosts=['my_site.com']
            ),
        ),
        Mount("/static/", StaticFiles(directory="static")),
        Mount("/media/", StaticFiles(directory="media")),
    ],
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', host="0.0.0.0", port=8000)
