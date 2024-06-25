from fastapi import APIRouter, Depends

from src.auth import jwt_auth

router = APIRouter()


@router.get('/courses', dependencies=[Depends(jwt_auth.JWTBearer(jwt_auth.JWTAuth()))])
async def get_courses():
    return {"message": "Hello World"}

