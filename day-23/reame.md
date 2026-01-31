## Day 23 - FastAPI MongoDB App

1. Installed Pydantic for models

2. Installed PyMongo to connect to MongoDB

3. Created a Todo model using Pydantic

4. Created routes for GET, POST, and PUT requests

5. Configured MongoDB connection in config/database.py

6. Added a serializer (schema.py) to convert MongoDB documents to JSON

7. Created Dockerfile to containerize the app

* Run the app with Docker:

```cmd
docker build -t fastapi-mongo-app .
docker run -p 8000:8000 fastapi-mongo-app