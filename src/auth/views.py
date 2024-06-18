from fastapi import APIRouter
from src.auth.tables import Profile

from src.auth import schemas

router = APIRouter()


@router.post('/user')
async def user_create(user_data: schemas.UserCreate):
    user = await Profile.create_user(username=user_data.username, password=user_data.password, active=True, role='admin', superuser=True, admin=True)
    return user


@router.get('/users')
async def get_users():
    users = await Profile.select()
    return users
