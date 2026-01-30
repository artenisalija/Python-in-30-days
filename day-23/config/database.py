from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:UTsbtxAhCdaPFvT1@day23mongo.3kjmio3.mongodb.net/?appName=day23mongo")

db = client.todo.db

collection_name = db["todo_collection"]