from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Boolean, String
from uuid import uuid4
from sqlalchemy.orm import relationship
from core.database import Base

class User(Base):
    __tablename__ = 'tb_users'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password_hash =  Column(String, unique=True)
    is_active = Column(Boolean, default=True)

    company = relationship('Company', back_populates='user')
    

