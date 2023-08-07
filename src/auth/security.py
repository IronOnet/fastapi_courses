from datetime import datetime, timedelta
from typing import Any, Union, Optional
from passlib.context import CryptContext

from jose import jwt, JWTError
from sqlalchemy.orm import Session
from src.auth import schemas

from src.auth.schemas import User

from .config import settings

import crud

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT (access token) based on the provided data"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check that hashed(plain_password) is equal to hashed_password"""
    return pwd_context.verify(plain_password, hashed_password)


def decode_token(token: str):
    """Return a dictionary that represents the decoded JWT"""
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])


def authenticate_user(db: Session, email: str, password: str) -> bool | User:
    user = crud.get_user_by_email_or_user_name(db, email)
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user
