from fastapi import APIRouter, Depends

from src.auth.crud import add_user_crud, user_exists_crud, user_login_crud
from src.auth.jwt_auth import JWTAuth
from src.auth.tables import Profile

from src.auth import schemas, jwt_auth

router = APIRouter()


@router.post('/user_registry')
async def user_create(user_data: schemas.UserAuth):
    if not await user_exists_crud(user_data.username):
        return await add_user_crud(user_data.dict())
    else:
        return {"error": "User already exists"}


@router.post('/user_login')
async def user_login(user_data: schemas.UserAuth):
    user = await user_login_crud(user_data.dict())
    if user:
        jwt_token = JWTAuth().sign_jwt(str(user.uuid), user.role)
        return jwt_token
    else:
        return {"error": "Username or password is incorrect"}


@router.get('/users', dependencies=[Depends(jwt_auth.JWTBearer(jwt_auth.JWTAuth()))])
async def get_users():
    users = await Profile.select()
    return users
