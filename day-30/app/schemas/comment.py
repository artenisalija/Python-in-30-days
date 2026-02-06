"""
Comment Pydantic schemas for request/response validation.
"""

from pydantic import BaseModel
from datetime import datetime
from app.schemas.user import User


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    post_id: int


class CommentInDB(CommentBase):
    id: int
    post_id: int
    author_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class Comment(CommentInDB):
    author: User
    
    class Config:
        from_attributes = True
