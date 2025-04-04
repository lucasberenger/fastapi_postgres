from sqlalchemy.orm import Session
from models.post_model import Post
from schemas.post_dto import PostCreateDTO, PostUpdateDTO

def create_post(db: Session, post_data: PostCreateDTO) -> Post:
    """Create Post"""
    db_post = Post(**post_data.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_post_by_id(db: Session, post_id: int) -> Post:
    """Get Post by ID"""
    return db.query(Post).filter(Post.id == post_id).first()