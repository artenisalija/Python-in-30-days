import psycopg2
import os

def get_connection():
    conn = psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST", "localhost"),
        database=os.environ.get("POSTGRES_DB", "food_logger"),
        user=os.environ.get("POSTGRES_USER", "user"),
        password=os.environ.get("POSTGRES_PASSWORD", "password"),
        port=os.environ.get("POSTGRES_PORT", "5432")
    )
    return conn
