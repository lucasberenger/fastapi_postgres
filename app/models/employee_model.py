from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Boolean, String, Numeric, ForeignKey
from uuid import uuid4
from sqlalchemy.orm import relationship
from core.database import Base

class Employee(Base):
    __tablename__ = 'tb_employees'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, index=True)
    role = Column(String, index=True)
    salary = Column(Numeric(10,2), nullable=False, index=True)

    company_id = Column(UUID(as_uuid=True), ForeignKey('tb_companies.id'))
    company = relationship('Company', back_populates='employees')