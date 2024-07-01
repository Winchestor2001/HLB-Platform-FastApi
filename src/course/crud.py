import base64
import os
from fastapi import HTTPException

from src.course.dry import course_poster_image
from src.course.tables import Course


async def create_course(data: dict, base_url):
    data = await course_poster_image(data, base_url)
    course = Course(**data)
    course.save().run_sync()
    return course.to_dict()


async def get_all_courses():
    courses = await Course.objects()
    return [course.to_dict() for course in courses]


async def course_exists(course_name: str):
    course = await Course.objects().get(Course.name == course_name)
    return course


async def course_detail(course_uuid: str):
    course = await Course.objects().get(Course.uuid == course_uuid)
    return course.to_dict() if course else None


async def update_course(course_uuid: str, data: dict, base_url: str):
    if data.get("poster_image", None):
        data = await course_poster_image(data, base_url)
        course = await Course.update(**data).where(Course.uuid == course_uuid).returning(*Course.all_columns())
        return course
    else:
        course = await Course.update(**data).where(Course.uuid == course_uuid).returning(*Course.all_columns())
        return course


async def delete_course(course_uuid: str):
    course = await Course.delete().where(Course.uuid == course_uuid).returning(Course.uuid)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
