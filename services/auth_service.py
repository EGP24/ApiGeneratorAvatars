from core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from pydantic import ValidationError
from schemas.user import UserSchema
from schemas.token import Token
from passlib.hash import bcrypt
from jose import jwt, JWTError
from db.users import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')


def get_current_user(token=Depends(oauth2_scheme)) -> UserSchema:
    return AuthService.validate_token(token)


class AuthService:
    def verify_password(self, plain_password, hash_password):
        return bcrypt.verify(plain_password, hash_password)

    def hash_password(self, password):
        return bcrypt.hash(password)

    def create_token(self, user: User) -> Token:
        user_data = UserSchema.from_orm(user)
        now = datetime.now()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
            'sub': str(user_data.id),
            'user': user_data.dict()
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return Token(access_token=token, token_type='Bearer')

    @staticmethod
    def validate_token(token) -> UserSchema:
        exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials')
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            raise exception

        user_data = payload.get('user')
        try:
            user = UserSchema.parse_obj(user_data)
        except ValidationError:
            raise exception

        return user
