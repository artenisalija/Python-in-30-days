from fastapi import FastAPI
from app.routers import auth, users

app = FastAPI(title="Day 21 - FastAPI with JWT")

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "FastAPI Tutorial with SQLAlchemy"}
