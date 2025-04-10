from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Boolean, String, Numeric, Date
from uuid import uuid4
from sqlalchemy.orm import relationship
from core.database import Base

class Investment(Base):
    __tablename__='tb_investments'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    sort = Column(String, index=True)
    value = Column(Numeric(10,2))
    application_date = Column(Date, index=True)