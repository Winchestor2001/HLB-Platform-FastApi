from piccolo.columns import ForeignKey, Integer, Varchar

from src.db.base import BaseModel


class User(BaseModel):
    username = Varchar(length=100)
    password = Varchar(length=100)
    role = Varchar(length=20)
