from piccolo.table import Table
from piccolo.columns import UUID, BigInt, Timestamp, Varchar
from settings import settings


class BaseModel(Table):
    uuid = UUID(primary_key=True)
    created_at = Timestamp(default=settings.get_tz)
    updated_at = Timestamp(default=settings.get_tz)

    class Meta:
        abstract = True


class Profile(BaseModel):
    username = Varchar(length=100)
    password = Varchar(length=100)
    role = Varchar(length=30, default='user')


