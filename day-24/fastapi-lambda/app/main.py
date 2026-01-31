from fastapi import FastAPI, HTTPException
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

db = {}

@app.post("/items/{item_id}")
def create_item(item_id: str, value: str):
    db[item_id] = value
    return {"item_id": item_id, "value": value}

@app.get("/items/{item_id}")
def read_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Not found")
    return {"item_id": item_id, "value": db[item_id]}

@app.put("/items/{item_id}")
def update_item(item_id: str, value: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Not found")
    db[item_id] = value
    return {"item_id": item_id, "value": value}

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Not found")
    del db[item_id]
    return {"status": "deleted"}
