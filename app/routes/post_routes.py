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
