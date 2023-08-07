import os
from typing import Optional, List

from fastapi import APIRouter, BackgroundTasks, HTTPException, Response, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.db.base import get_db
from src.auth import crud, schemas, security
from src.dependencies import get_current_user

users_router = APIRouter(prefix="/users", tags=["user"])
auth_router = APIRouter(tags=["aut"])


@auth_router.post("/token")
async def login(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """User will attempt to authenticate with email/password flow"""

    user = security.authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="incorrect username or password",
        )

    token = security.create_access_token(data={"sub": user.email})
    response.set_cookie(
        key="Authorization",
        value=f"Bearer {token}",
        samesite="Lax" if "dev" in os.environ.get("ENV") else "None",
        domain="localhost",
        secure="dev",
        httponly=True,
        max_age=60 * 30,
        expires=60 * 30,
    )

    return {"access_token": token, "tokey_type": "bearer"}


@auth_router.post("/logout")
async def logout_and_expire_cookie(
    response: Response, current_user: schemas.User = Depends(get_current_user)
):
    response.set_cookie(
        key="Authorization",
        vaue=f"",
        samesite="Lax",
        domain="localhost",
        secure="dev",
        httponly=True,
        max_age=1,
        expires=1,
    )

    return {}


@users_router.get("", response_model=List[schemas.UserResponse])
def get_one_or_all_users(
    user_id: Optional[int] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """Return either all users, or a single user with id == userId. Always returns a list"""

    if user_id:
        users = [crud.get_user_by_id(db, user_id)]
    else:
        users = crud.get_users(db, skip=skip, limit=limit)

    return [
        schemas.UserResponse(
            id=user.id,
            email=user.email,
            username=user.first_name + " " + user.last_name,
        )
        for user in users
    ]


@users_router.get("/me", response_model=schemas.User)
def get_authenticated_user(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    """Get the currently logged in user if there is one (testing purposes only)"""
    return current_user


@users_router.post("", response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate, bg_tasks: BackgroundTasks, db: Session = Depends(get_db)
):
    """Create a new user record in the database and send a registration confirmation
    email."""

    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="email already exists"
        )

    # TODO: Add background task here to send confirmation link
    # to the user's email address

    new_user: schemas.User = crud.create_user(db=db, user=user)

    return new_user


@users_router.put("", response_model=schemas.UserUpdateRequestBody)
def update_user(
    request_body: schemas.UserUpdateRequestBody,
    db: Session = Depends(get_db),
    current_user: schemas.UserWithPassword = Depends(get_current_user),
):
    """Update an authenticated user's current username and/or bio."""

    if not security.verify_password(
        request_body.password, current_user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="wrong password"
        )

    # Check if they are trying to update the username
    if request_body.new_username is not None:
        existing_user = crud.get_user_by_username(db, request_body.new_username)
        if existing_user is not None:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="username already exists",
            )

        # Update user attributes
        user = crud.update_user(db, current_user.id, request_body)
        return user


@users_router.delete("/", response_model=schemas.EmptyResponse)
def delete(
    request_body: schemas.UserDeleteRequestBody,
    db: Session = Depends(get_db),
    current_user: schemas.UserWithPassword = Depends(get_current_user),
):
    if not security.verify_password(
        request_body.password, current_user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="wrong password"
        )
    crud.delete_user(db, current_user.id)

    return schemas.EmptyResponse()
