from fastapi import FastAPI
from dotenv import load_dotenv

from src.auth.router import users_router, auth_router
from src.db.base import create_tables

app = FastAPI

load_dotenv()

## If the database is empty

try: 
    create_tables() 
except Exception as e: 
    print("Error occurred while creating tables ", e)


app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
def root():
    return {"message": "Welcome to the course management API!"}
