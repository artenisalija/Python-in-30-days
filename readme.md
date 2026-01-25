# FastAPI Health Check App

This project is a minimal FastAPI application created to demonstrate a basic API setup and deployment workflow.

## What This App Does
- Runs a FastAPI server
- Exposes a `/health` endpoint
- Returns a simple JSON response to confirm the service is running

## Endpoint
- `GET /health`
- Response:
```json
{ "status": "ok" }
