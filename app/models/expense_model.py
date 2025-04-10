from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, ForeignKey, Date, Numeric, Enum
from uuid import uuid4
from sqlalchemy.orm import relationship
from core.database import Base
from enum import Enum as PyEnum

class Status(PyEnum):
    PENDING = 'pending'
    PAYED = 'payed'
    EXPIRED = 'expired'


class Expense(Base):
    __tablename__='tb_expenses'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=False, index=True)
    value = Column(Numeric(10,2), nullable=False, index=True)
    due_date = Column(Date, nullable=False, index=True)
    status = Column(Enum(Status), default=Status.PENDING)

    company_id = Column(UUID(as_uuid=True), ForeignKey('tb_companies.id'))
    company = relationship('Compnay', back_populates='expenses')