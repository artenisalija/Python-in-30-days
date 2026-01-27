# Day 20 – CRUD FastAPI Using SQLAlchemy

In this project I built a simple CRUD API using FastAPI and SQLAlchemy.

## Setup

First, I added all required dependencies such as SQLAlchemy, Pydantic, FastAPI, and typing.

## Steps Completed

1. Created the FastAPI application  
2. Set up the database connection  
3. Created the database model  
4. Created Pydantic models (data classes)  
5. Implemented CRUD operations:
   - Get user by ID  
   - Create user  
   - Update user  
   - Delete user  
   - Get all users  
6. Created a Dockerfile to build an image and run the app in a container  
7. Created a `requirements.txt` file for all dependencies  

## Build and Run with Docker

```cmd
docker build -t day_20 .
docker run -p 8000:8000 day_20
