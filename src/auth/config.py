import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")


settings = Settings()
