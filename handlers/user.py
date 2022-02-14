from fastapi import APIRouter, Depends, HTTPException, status, Response
from schemas.user import UserCreateSchema, UserLoginSchema
from schemas.token import Token
from aiohttp.client_exceptions import ClientConnectorError
from aiohttp import ClientSession
from services.user_service import UserService
from services.auth_service import AuthService, get_current_user
from db.users import User

router = APIRouter()


@router.post('/registration', response_model=Token)
async def registration(schema: UserCreateSchema, u_service: UserService = Depends(UserService), a_service: AuthService = Depends(AuthService)):
    user = await u_service.get_by_username(schema.username)
    if user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='This username is registered')
    user = await u_service.create_user(a_service, schema)
    return a_service.create_token(user)


@router.post('/login', response_model=Token)
async def login(schema: UserLoginSchema, service: UserService = Depends(UserService), a_service: AuthService = Depends(AuthService)):
    user = await service.get_by_username(schema.username)
    if user is None or not a_service.verify_password(schema.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
    return a_service.create_token(user)


@router.get('/avatar')
async def get_avatar(user: User = Depends(get_current_user), service: UserService = Depends(UserService)):
    avatar_data = await service.get_avatar_by_username(user.username)
    if avatar_data is None:
        async with ClientSession() as client:
            try:
                response = await client.get(f'http://image_generator:8080/monster/{user.username}')
            except ClientConnectorError:
                raise HTTPException(status_code=status.HTTP_423_LOCKED, detail='Service is temporarily unavailable')
            avatar_data = await response.content.read()
            await service.set_avatar_by_username(user.username, avatar_data)
    return Response(content=avatar_data, media_type='image/png')
