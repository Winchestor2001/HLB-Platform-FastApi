from fastapi import APIRouter, Depends

from src.course import schemas
from src.course.crud import create_course, course_exists

router = APIRouter()


@router.post('/create_course')
async def user_create(course_data: schemas.CourseModel):
    if not await course_exists(course_data.name):
        return await create_course(course_data.dict())
    else:
        return {"error": "Course already exists"}
