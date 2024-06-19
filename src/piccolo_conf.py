from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

from settings import settings

DB = PostgresEngine(
    config={
        "database": settings.DB_NAME,
        "user": settings.DB_USER,
        "password": settings.DB_PASSWORD,
        "host": settings.DB_HOST,
        "port": settings.DB_PORT,
    }
)

# A list of paths to piccolo apps
# e.g. ['blog.piccolo_app']
APP_REGISTRY = AppRegistry(
    apps=[
        "piccolo_admin.piccolo_app",
        "piccolo_api.token_auth.piccolo_app",
        "auth.piccolo_app",
    ]
)
