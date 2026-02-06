"""
Post Pydantic schemas for request/response validation.
"""

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.schemas.user import User


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class PostInDB(PostBase):
    id: int
    author_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class Post(PostInDB):
    author: User
    
    class Config:
        from_attributes = True


class PostWithComments(Post):
    comments: List["Comment"] = []
    
    class Config:
        from_attributes = True


# Import Comment here to avoid circular import
from app.schemas.comment import Comment
PostWithComments.model_rebuild()
