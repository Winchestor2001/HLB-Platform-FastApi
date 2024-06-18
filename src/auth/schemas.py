from enum import Enum

from pydantic import BaseModel


class UserRole(str, Enum):
    user = 'user'
    admin = 'admin'


class UserCreate(BaseModel):
    username: str
    password: str
    role: UserRole = UserRole.user
