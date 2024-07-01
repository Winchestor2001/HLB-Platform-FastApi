from src.course.tables import Course


async def create_course(data: dict):
    course = Course(**data)
    course.save().run_sync()
    return course.to_dict()


async def course_exists(course_name: str):
    course = await Course.objects().get(Course.name == course_name)
    return course
