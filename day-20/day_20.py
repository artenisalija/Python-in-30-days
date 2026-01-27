from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Optional

app = FastAPI(title="Day 20 API - Integration with SQL", version="1.0.0")

# Database setup
DATABASE_URL = "sqlite:///./users.db"  # Using SQLite for simplicity
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) # SQLite specific
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#Database model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String, index=True)

Base.metadata.create_all(engine)

# Pydantic models (DataClasses)
class UserCreate(BaseModel):
    name: str
    email: str
    role: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

get_db()



#CRUD Operations
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to Day 20 API - Integration with SQL"}

#Get User by ID
@app.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail={"error": "User not found"})
    return user

#Create User
@app.post("/users/", response_model=UserResponse, tags=["Users"])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail={"error": "Email already registered"})
    
    # Create new user
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#Update User
@app.put("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail={"error": "User not found"})
    
    # Update user details
    existing_user.name = user.name
    existing_user.email = user.email
    existing_user.role = user.role
    db.commit()
    db.refresh(existing_user)
    return existing_user

#Delete User
@app.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail={"error": "User not found"})
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

#Get all users
@app.get("/users/", response_model=List[UserResponse], tags=["Users"])
def get_all_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

    