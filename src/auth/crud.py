from typing import Union, List

from sqlalchemy.orm import Session
from sqlalchemy import or_, func, case, column
from sqlalchemy.exc import SQLAlchemyError
from src.auth import schemas, security


from src.models import User
from src.auth import exceptions


def get_user_by_id(db: Session, user_id: int) -> Union[User, None]:
    """
    Get a single user by id"""
    try:
        query = db.query(User).filter(User.id == user_id).one_or_none()
    except SQLAlchemyError as e:
        raise exceptions.UserNotFoundException(f"could not find user: {e}")
    return query


def get_user_by_email_or_user_name(db, email: str) -> User:
    """
    Get a single user by email"""
    try:
        user = (
            db.query(User)
            .filter(func.lower(User.email) == func.lower(email))
            .one_or_none()
        )
    except SQLAlchemyError as e:
        raise exceptions.UserNotFoundException(f"could not find user: {e}")

    return user


def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).one_or_none()


def search_user_by_username_fragment(
    db: Session, username_fragment: str, skip: int = 0, limit: int = 100
) -> List[User]:
    return (
        db.query(User)
        .filter(User.username.ilike(f"%{username_fragment}%"))
        .limit(limit)
        .offset(skip)
    )


def get_user_by_email_or_username(db: Session, email: str):
    """Get A single user by email or username"""
    query = db.query(User).filter(
        or_(
            func.lower(User.email) == func.lower(email),
            func.lower(User.username) == func.lower(email),
        )
    )
    return query.first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Get all users"""
    query = db.query(User).offset(skip).limit(limit)
    return query.all()


def create_user(db: Session, user: schemas.UserCreate) -> User:
    """Creates an instance of a user and stores it
    in the database"""
    user_instance = User(
        email=user.email.lower(),
        username=user.username.lower(),
        password_hash=security.get_password_hash(user.password),
    )
    db.add(user_instance)
    db.commit()
    db.refresh(user_instance)
    return user_instance


def update_user(
    db: Session, user_id: int, user_update: schemas.UserUpdateRequestBody
) -> User:
    actual_user = db.query(User).filter(User.id == user_id).one_or_none()

    if user_update.new_username:
        actual_user.username = user_update.new_username
    if user_update.password:
        actual_user.password_hash = security.get_password_hash(user_update.password)
    db.commit()
    db.refresh(actual_user)
    return actual_user
