from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.auth_utils import hash_password, verify_password
from auth.auth_handler import create_access_token 
from core.database import get_db
from models.user_model import User
from schemas.user_dto import UserCreateDTO, UserResponseDTO
from schemas.login_dto import LoginDTO
from services.user_service import get_user_by_email, create_user

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post('/register', response_model=UserResponseDTO)
async def register_user(user: UserCreateDTO, db: Session = Depends(get_db)):
    """Register a new user"""
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail='Email already registered')
    user.password = hash_password(user.password)
    new_user = create_user(db, user)

    return new_user

@router.post('/login')
async def login(user: LoginDTO, db: Session = Depends(get_db)):
    """Login user and return JWT token"""
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail='Invalid credentials')

    access_token = create_access_token(data={'sub': db_user.email})
    return {'access_token': access_token, 'token_type': 'bearer'}