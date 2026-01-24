from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Simple FastAPI Backend")

# In-memory "database"
users = []
current_id = 1

# Schemas
class UserCreate(BaseModel):
    name: str
    email: str

class User(UserCreate):
    id: int

# Health check
@app.get("/")
def root():
    return {"status": "ok", "message": "API is running"}

# Create user
@app.post("/users", response_model=User)
def create_user(user: UserCreate):
    global current_id
    new_user = User(id=current_id, name=user.name, email=user.email)
    users.append(new_user)
    current_id += 1
    return new_user

# Read all users
@app.get("/users", response_model=List[User])
def get_users():
    return users

# Read one user
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Update user
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated: UserCreate):
    for user in users:
        if user.id == user_id:
            user.name = updated.name
            user.email = updated.email
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    for user in users:
        if user.id == user_id:
            users = [u for u in users if u.id != user_id]
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
