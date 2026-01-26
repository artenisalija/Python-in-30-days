# Day 19 – Creating a Simple RESTful API Using FastAPI

This project demonstrates the basics of building a RESTful API with FastAPI.

## Steps Implemented

1. Imported FastAPI.  
2. Created a dictionary with simple sample data.  
3. Implemented a basic “Hello World” endpoint at the root path.  
4. Added a GET endpoint to return the dictionary data, including error handling when a user is not found.  
5. Created a class to initialize a function for creating a user.  
6. Created a class to update a user.  
7. Implemented a POST endpoint to create a new user.  
8. Implemented a PUT endpoint to update an existing user.  
9. Implemented a DELETE endpoint to remove a user.  
10. Implemented a GET endpoint to search users by name.

## Running the Application

Use the following command to start the development server:

```cmd
python -m uvicorn app:app --reload
