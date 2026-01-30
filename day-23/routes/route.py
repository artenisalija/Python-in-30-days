from fastapi import APIRouter
from models.todo import Todo
from config.database import collection_name
from schema.schema import list_serial
from bson import ObjectId

router = APIRouter()

# Get Request Method
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos

# Post Request
@router.post("/")
async def create_todo(todo: Todo):
    todo_dict = todo.model_dump()
    result = collection_name.insert_one(todo_dict)
    return {"id": str(result.inserted_id)}

# Put Request
@router.put("/{id}")
async def update_todo(id: str, todo: Todo):
    todo_dict = todo.model_dump()
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": todo_dict}
    )
    return {"status": "updated"}

# Delete Request
@router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "deleted"}
    