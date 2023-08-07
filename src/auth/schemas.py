from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    role: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserWithPassword(User):
    hashed_password: str


class UserUpdateRequestBody(BaseModel):
    password: str
    new_username: Optional[str]


class UserResponse(BaseModel):
    id: int
    email: str
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class EmptyResponse(BaseModel):
    """Empty HTTP Response"""

    pass


class UserDeleteRequestBody(BaseModel):
    password: str
