from sqlalchemy import Column, String, Boolean, DateTime, func
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from .database import Base

class Domain(Base):
    __tablename__ = "domains"

    domain_id = Column(UUID, primary_key=True, default=uuid4)
    domain_name = Column(String, index=True)
    created_time = Column(DateTime, default=datetime.utcnow)
    https_enabled = Column(Boolean, default=False)