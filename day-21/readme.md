# Day 21 – CRUD FastAPI Using JWT and OAuth

In this project I built a simple CRUD API using FastAPI and SQLAlchemy.

## Setup

First, I added all required dependencies such as SQLAlchemy, Pydantic, FastAPI, JWT, OAuth, Passlib into the ppython file but didnt install dependencies to run it with a docker container

## Steps Completed

1. Created the FastAPI application  
2. Added hashed_pwd and is_active to class
3. Created new pytendic model for User Update 
4. Created Security Functions  
5. Set up Authentication Dependency
6. Added the Active user function to all the CRUD calls
7. Created a Dockerfile to build an image and run the app in a container   

## Build and Run with Docker

```cmd
docker build -t day_20 .
docker run -p 8000:8000 day_20
