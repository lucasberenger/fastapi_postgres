from sqlalchemy.orm import Session
from models.user_model import User
from schemas.user_dto import UserCreateDTO, UserUpdateDTO


def get_all_users(db: Session) -> list[User]:
    """Get all users from the database."""
    return db.query(User).all()


def create_user(db: Session, user_data: UserCreateDTO) -> User:
    """Create a new user in the database."""
    user = User(**user_data.model_dump())
    db.add(user)
    db.commit() 
    db.refresh(user)
    return user

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