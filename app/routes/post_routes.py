from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.post_dto import PostCreateDTO, PostUpdateDTO, PostResponseDTO
from core.database import get_db
from services import post_service
from typing import List

router = APIRouter(prefix='/posts', tags=['Posts'])

@router.post('/', response_model=PostResponseDTO)
async def create_post(post: PostCreateDTO, db: Session = Depends(get_db)):
    """ Create a new Post """
    new_post = post_service.create_post(db, post)
    return new_post

@router.get('/{post_id}', response_model=PostResponseDTO)
async def get_post(post_id: int, db: Session = Depends(get_db)):
    """Get Post by ID"""
    post = post_service.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.get('/user/{user_id}', response_model=List[PostResponseDTO])
async def get_posts_by_user(user_id: int, db: Session = Depends(get_db)):
    """"Get Posts by User ID"""
    posts = post_service.get_posts_by_user(db, user_id)
    if not posts:
        raise HTTPException(status_code=404, detail="No posts found for this user")
    return posts