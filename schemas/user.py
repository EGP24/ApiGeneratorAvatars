from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    username: str
    password: str


class UserLoginSchema(UserCreateSchema):
    pass
