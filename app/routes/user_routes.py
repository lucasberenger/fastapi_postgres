from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.user_dto import UserCreateDTO, UserResponseDTO
from models.user_model import User
from core.database import get_db
from typing import List

router = APIRouter(prefix='/user', tags=['User'])

@router.get('/', response_model=List[UserResponseDTO])
async def get_users(db: Session = Depends(get_db)):
    """Get all users."""
    return db.query(User).all()

@router.post('/', response_model=UserResponseDTO)
async def create_user(user: UserCreateDTO, db: Session = Depends(get_db)):
    """Create a new user."""
    db_user = User(name=user.name, email=user.email, password=user.password, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user