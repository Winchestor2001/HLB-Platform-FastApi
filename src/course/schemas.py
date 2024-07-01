from typing import Optional

from pydantic import BaseModel


class CourseModel(BaseModel):
    name: Optional[str] = None
    poster_image: Optional[str] = None
    paid: Optional[bool] = None
    price: Optional[float] = None
