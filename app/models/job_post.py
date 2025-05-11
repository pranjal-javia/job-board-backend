import enum

from sqlalchemy import Column, UUID, String, ForeignKey, DateTime, func

from .user import User
from app.db import Base

class RecruitmentTag(enum.Enum):
    open = "open"
    close = "close"

class JobPost(Base):
    __tablename__ = "job_post"
    id = Column(UUID, primary_key=True)
    recruiter_id = Column(UUID, ForeignKey(User.id), nullable=False)
    company_name = Column(String, nullable=False)
    company_mail = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    role = Column(String, nullable=False)
    location = Column(String, nullable=False)
    employement_type = Column(String, nullable=False)
    description = Column(String, nullable=True)
    recruitment_tag = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True))