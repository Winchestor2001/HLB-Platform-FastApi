from piccolo.table import Table
from piccolo.columns import UUID, Timestamp

from src.settings import settings


class BaseModel(Table):
    uuid = UUID(primary_key=True)
    created_at = Timestamp(default=settings.get_tz)
    updated_at = Timestamp(default=settings.get_tz)

    class Meta:
        abstract = True
