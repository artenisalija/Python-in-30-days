Day-12: FastAPI + Docker

- Built a **FastAPI app** in `day_12.py` and added `requirements.txt`.
- Created a **Dockerfile optimized for layering**:
  - `requirements.txt` copied **first** → enables **layer caching**.
  - App code copied **after** → only this layer rebuilds when changed.
  - Uses **python:3.11-slim** + `--no-cache-dir` → smaller image.
- Now the app runs **fully in Docker** with `uvicorn` included, no local Python needed.

How to run

```bash
docker build -t day-12-fastapi .
docker run -p 8000:8000 day-12-fastapi
