from sqlalchemy import Column, UUID, String, ForeignKey, DateTime, func, Date, Enum

from app.db import Base
from .user import User
from .job_post import JobPost

class SavedJob(Base):
    __tablename__ = "saved_job"
    id = Column(UUID, primary_key=True)
    applicant_id = Column(UUID, ForeignKey(User.id), nullable=False)
    job_id = Column(UUID, ForeignKey(JobPost.id), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())