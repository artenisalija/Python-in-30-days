from fastapi import FastAPI, Path, status
from typing import Optional
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app = FastAPI()

users = {
    1: {"name": "Alice", "role": "developer", "website": "alice.com", "age": 30}
}

class User(BaseModel):
    name: str
    role: str
    website: str
    age: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    website: Optional[str] = None
    age: Optional[int] = None

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/users/{user_id}")
def get_user(user_id: int = Path(..., title="The ID of the user to get", gt=0)):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.post("/users/{user_id}", status_code=status.HTTP_201_CREATED)
def create_user(user_id: int, user: User):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user_id] = user.dict()
    return users[user_id]

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    current_user = users[user_id]
    if user.name is not None:
        current_user["name"] = user.name
    if user.role is not None:
        current_user["role"] = user.role   
    if user.website is not None:
        current_user["website"] = user.website
    if user.age is not None:
        current_user["age"] = user.age
    return current_user

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = users.pop(user_id)
    return ["Deleted user:", deleted_user]

@app.get("/users/search")
def search_users(name: Optional[str] = None, role: Optional[str] = None):
    results = []
    for user in users.values():
        if name is not None and user["name"] != name:
            continue
        if role is not None and user["role"] != role:
            continue
        results.append(user)
    return results