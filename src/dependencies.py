from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2
from jose import JWTError
from sqlalchemy.orm import Session

from src.auth import schemas, security
from src.db.base import get_db
from src.auth import crud

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/token")

invalid_credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="invalid credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
    """ "
    Decode the provided jwt and extract the user using the [sub] field"""

    token_data: schemas.TokenData = None

    if not token:
        return None
    try:
        payload = security.decode_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise invalid_credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise invalid_credentials_exception

    user = crud.get_user_by_email(db, token_data.email)
    if user is None:
        raise invalid_credentials_exception
    return user
