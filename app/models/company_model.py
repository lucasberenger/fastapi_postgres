from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey
from uuid import uuid4
from sqlalchemy.orm import relationship
from core.database import Base

class Company(Base):
    __tablename__ = 'tb_companies'
    
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String, nullable=False, index=True)
    cnpj = Column(String, unique=True)

    user_id = Column(UUID(as_uuid=True), ForeignKey('tb_users.id'))
    user = relationship('User', back_populates='company')

    employees = relationship('Employee', back_populates='company')
    taxes = relationship('Tax', back_populates='company')
    expenses = relationship('Expense', back_populates='company')
    investments = relationship('Investment', back_populates='company')