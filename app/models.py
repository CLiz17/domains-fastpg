from sqlalchemy import Column, String, Boolean, DateTime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from .database import Base

class Domain(Base):
    __tablename__ = "domains"

    domain_id = Column(UUID, primary_key=True, default=uuid4)
    domain_name = Column(String(255), unique=True, nullable=False)
    created_time = Column(DateTime, default=func.now())
    https_enabled = Column(Boolean, default=False)