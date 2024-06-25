from enum import Enum

from pydantic import BaseModel


class UserAuth(BaseModel):
    username: str
    password: str
