from sqlalchemy.orm import Session
from models.user_model import User
from schemas.user_dto import UserCreateDTO, UserUpdateDTO
from auth.auth_utils import hash_password


def get_all_users(db: Session) -> list[User]:
    """Get all users from the database."""
    return db.query(User).all()


def create_user(db: Session, user_data: UserCreateDTO) -> User:
    """Create a new user in the database."""
   
    hashed_password = hash_password(user_data.password)

    user = User(
        name=user_data.name,
        email=user_data.email,
        password_hash=hashed_password
    )

    db.add(user)
    db.commit() 
    db.refresh(user)
    return user

#TODO: testar criação de usuário

def edit_user(db: Session,  user_id: int, user_data: UserUpdateDTO) -> User:
    """Edit a user by ID"""
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        return None
    
    for key, value in user_data.model_dump(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user
    

def get_user_by_id(db: Session, user_id: int) -> User:
    """Get a user by ID."""
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> User:
    """Get a user by email"""
    return db.query(User).filter(User.email == email).first()


def delete_user(db: Session, user_id: int) -> bool:
    """Delete user by ID"""
    user = db.query(User).filter(User.id == user_id).first()
    if user is None: 
        return False
    db.delete(user)
    db.commit()
    return True