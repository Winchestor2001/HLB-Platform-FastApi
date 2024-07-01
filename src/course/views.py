from fastapi import APIRouter, Depends, Request, status

from src.course import schemas
from src.course.crud import create_course, course_exists, course_detail, update_course, delete_course, get_all_courses

router = APIRouter()


def get_base_url(request: Request):
    return str(request.base_url)


@router.post('/create_course')
async def user_create(course_data: schemas.CourseModel, request: Request):
    if not await course_exists(course_data.name):
        base_url = get_base_url(request=request)
        course = await create_course(course_data.dict(exclude_unset=True), base_url)
        return course
    else:
        return {"error": "Course already exists"}


@router.get("/get_all_courses")
async def get_all_courses_handler():
    courses = await get_all_courses()
    return courses


@router.get('/course_detail/{uuid}')
async def course_detail_handler(uuid: str):
    course = await course_detail(course_uuid=uuid)
    return course


@router.patch('/update_course/{uuid}')
async def update_course_handler(course_data: schemas.CourseModel, request: Request, uuid: str):
    base_url = get_base_url(request=request)
    course = await update_course(uuid, course_data.dict(exclude_unset=True), base_url)
    return course


@router.delete('/delete_course/{uuid}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_course_handler(uuid: str):
    course = await delete_course(uuid)
    return course
