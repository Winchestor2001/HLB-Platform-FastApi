from fastapi import APIRouter
from src.auth.views import router as auth_router
from src.course.views import router as course_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix='/auth', tags=['Auth'])
api_router.include_router(course_router, prefix='/course', tags=['Course'])

