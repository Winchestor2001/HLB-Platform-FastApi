from pydantic_settings import BaseSettings
import pytz
from datetime import datetime


class Settings(BaseSettings):
    """
    Settings for the application.
    """
    HOST: str = 'localhost'
    PORT: int = 8000

    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = 'postgres888'
    DB_NAME: str = 'hlb_database'

    TZ: str = 'Asia/Tashkent'

    def get_tz(self):
        tz = pytz.timezone(self.TZ)
        return datetime.now(tz)

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
