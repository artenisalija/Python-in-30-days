from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "fooddb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")

def get_conn():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.get("/foods")
def get_foods():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM food;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1]} for r in rows]

@app.post("/foods/{name}")
def add_food(name: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO food (name) VALUES (%s);", (name,))
    conn.commit()
    cur.close()
    conn.close()
    return {"status": "added", "food": name}

@app.delete("/foods/{food_id}")
def delete_food(food_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM food WHERE id = %s;", (food_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"status": "deleted", "id": food_id}
