from fastapi import APIRouter
from src.auth.views import router as auth_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix='/auth', tags=['Auth'])

