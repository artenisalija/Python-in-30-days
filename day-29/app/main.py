from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World from Day 29 - Updated via CI/CD!", "version": "v2"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}