from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class User(Base):
    __tablename__ = 'tb_user'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password= Column(String, unique=True)
    age = Column(Integer)
    is_active = Column(Boolean, default=True)
    posts = relationship('Post', back_populates='author')

