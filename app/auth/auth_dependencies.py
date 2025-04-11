from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from core.database import get_db
from .auth_handler import decode_access_token
from models.user_model import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    """Get current user from token"""
    payload = decode_access_token(token)
    email: str = payload.get('sub')

    if email is None:
        raise HTTPException(status_code=401, detail='Invalid credentials')
    
    user = db.query(User).filter(User.email == email).first()

    if user is None:
        raise HTTPException(status_code=401, detail='User not found')

    return user