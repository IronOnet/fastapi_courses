from fastapi import FastAPI

from src.auth.router import users_router, auth_router

app = FastAPI

app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
def root():
    return {"message": "Welcome to the course management API!"}
