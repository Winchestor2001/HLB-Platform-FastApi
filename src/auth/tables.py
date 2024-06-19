from piccolo.apps.user.tables import BaseUser
from piccolo.table import Table
from piccolo.columns import UUID, BigInt, Timestamp, Varchar, Secret, Boolean, Timestamptz
from settings import settings


class BaseMixin:
    uuid = UUID(primary_key=True)
    created_at = Timestamptz(default=settings.get_tz())
    updated_at = Timestamptz(default=settings.get_tz())


class Profile(BaseMixin, Table):
    username = Varchar(length=100, unique=True)
    password = Secret(length=255)
    full_name = Varchar(null=True)
    phone_number = Varchar(length=255, null=True)
    role = Varchar(length=50, default='user')
