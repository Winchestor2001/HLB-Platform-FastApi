from pydantic import BaseModel


class CourseModel(BaseModel):
    name: str
    poster_image: str
    paid: bool
    price: float
