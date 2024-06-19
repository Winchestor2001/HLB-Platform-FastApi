from src.auth import schemas
from src.auth.tables import Profile


async def add_user_crud(data: dict):
    user = Profile(**data)
    user.save().run_sync()
    return user.to_dict()


async def user_exists_crud(username: str):
    user = Profile.objects().get(Profile.username == username).run_sync()
    return user.exists()


async def user_login_crud(data: dict):
    username, password = data['username'], data['password']
    user = await Profile.objects().get(Profile.username == username)
    print(user.to_dict())
