"""
Comment API endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.user import User as UserModel
from app.models.comment import Comment as CommentModel
from app.models.post import Post as PostModel
from app.schemas.comment import Comment, CommentCreate
from app.api.auth import get_current_user

router = APIRouter()


@router.get("/post/{post_id}", response_model=List[Comment])
def get_post_comments(post_id: int, db: Session = Depends(get_db)):
    """Get all comments for a specific post."""
    comments = db.query(CommentModel).filter(
        CommentModel.post_id == post_id
    ).all()
    return comments


@router.post("/", response_model=Comment, status_code=status.HTTP_201_CREATED)
def create_comment(
    comment_in: CommentCreate,
    current_user: UserModel = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new comment on a post."""
    # Check if post exists
    post = db.query(PostModel).filter(PostModel.id == comment_in.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    
    db_comment = CommentModel(
        content=comment_in.content,
        post_id=comment_in.post_id,
        author_id=current_user.id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(
    comment_id: int,
    current_user: UserModel = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a comment."""
    comment = db.query(CommentModel).filter(CommentModel.id == comment_id).first()
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found"
        )
    
    # Check if user is the author
    if comment.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this comment"
        )
    
    db.delete(comment)
    db.commit()
    return None
