from src.auth import schemas
from src.auth.tables import Profile


async def add_user_crud(data: dict):
    data['password'] = Profile.get_password_hash(data['password'])
    user = Profile(**data)
    user.save().run_sync()
    return user.to_dict()


async def user_exists_crud(username: str):
    user = await Profile.objects().get(Profile.username == username)
    return user


async def user_login_crud(data: dict):
    username, password = data['username'], data['password']
    user_info = await Profile.objects().get(Profile.username == username)
    valid_password = Profile.verify_password(password, user_info.password)
    if valid_password:
        return user_info
    return False
