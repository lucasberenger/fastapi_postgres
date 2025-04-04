from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.user_dto import UserCreateDTO, UserResponseDTO, UserUpdateDTO
from core.database import get_db
from services import user_service
from typing import List

router = APIRouter(prefix='/user', tags=['User'])

@router.get('/', response_model=List[UserResponseDTO])
async def get_users(db: Session = Depends(get_db)):
    """Get all users."""
    return user_service.get_all_users(db)

@router.post('/', response_model=UserResponseDTO)
async def create_user(user: UserCreateDTO, db: Session = Depends(get_db)):
    """Create a new user."""
    return user_service.create_user(db, user)

@router.get('/{user_id}', response_model=UserResponseDTO)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """Get a user by Id"""
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user

@router.put('/{user_id}', response_model=UserResponseDTO)
async def edit_user(user_id: int, user: UserUpdateDTO, db: Session = Depends(get_db)):
    """Edit user by Id"""
    user = user_service.edit_user(db, user_id, user)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user

@router.delete('/{user_id}', status_code=200)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete user by Id"""
    user = user_service.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    return {'message': 'User deleted successfully'}