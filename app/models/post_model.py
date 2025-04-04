from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base


class Post(Base):
    __tablename__ = 'tb_post'

    id = Column(Integer,primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('tb_user.id'))
    author = relationship('User', back_populates='posts')
    