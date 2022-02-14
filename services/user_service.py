from services.auth_service import AuthService
from schemas.user import UserCreateSchema
from ormar.exceptions import NoMatch
from db.database import redis
from db.users import User
from fastapi import Depends


class UserService:
    async def get_by_username(self, username):
        try:
            user = await User.objects.get(username=username)
        except NoMatch:
            user = None
        return user

    async def create_user(self, a_service: AuthService, schema: UserCreateSchema):
        hashed_password = a_service.hash_password(schema.password)
        user = await User.objects.create(username=schema.username, password=hashed_password)
        return user

    async def get_avatar_by_username(self, username):
        avatar_data = await redis.get(username)
        return avatar_data

    async def set_avatar_by_username(self, username, avatar_data):
        await redis.set(username, avatar_data)
