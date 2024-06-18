from piccolo.apps.user.tables import BaseUser
from piccolo.table import Table
from piccolo.columns import UUID, BigInt, Timestamp, Varchar, Secret, Boolean
from settings import settings


class BaseMixin:
    uuid = UUID(primary_key=True)
    created_at = Timestamp(default=settings.get_tz)
    updated_at = Timestamp(default=settings.get_tz)


class Profile(BaseUser, Table):
    _min_password_length = 3
    _max_password_length = 32

    username = Varchar(length=100, unique=True)
    password = Secret(length=255)
    first_name = Varchar(null=True)
    last_name = Varchar(null=True)
    email = Varchar(length=255)
    role = Varchar(length=50, default='user')
    active = Boolean(default=False)
    admin = Boolean(
        default=False, help_text="An admin can log into the Piccolo admin GUI."
    )
    superuser = Boolean(
        default=False,
        help_text=(
            "If True, this user can manage other users's passwords in the "
            "Piccolo admin GUI."
        ),
    )
    last_login = Timestamp(
        null=True,
        default=None,
        required=False,
        help_text="When this user last logged in.",
    )
