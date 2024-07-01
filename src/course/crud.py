import base64
import os
from fastapi import HTTPException
from src.course.tables import Course


async def create_course(data: dict, base_url):
    image_data = base64.b64decode(data["poster_image"])

    file_name = f"{data['name']}_poster.png"
    file_path = f"media/course_posters/{file_name}"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(image_data)

    data.pop("poster_image")
    image_path = f"{base_url}media/course_posters/{file_name}"

    course = Course(poster_image=image_path, **data)
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
        image = data.pop("poster_image")
        image_data = base64.b64decode(image)

        file_name = f"{data['name']}_poster.png"
        file_path = f"media/course_posters/{file_name}"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(image_data)

        image_path = f"{base_url}media/course_posters/{file_name}"
        data.update({"poster_image": image_path})
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
