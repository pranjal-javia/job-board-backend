from sqlalchemy import Column, UUID, ForeignKey, DateTime, func

from app.db import Base
from .user import User
from .job_post import JobPost

class JobApplication(Base):
    __tablename__ = "job_application"
    id = Column(UUID, primary_key=True)
    applicant_id = Column(UUID, ForeignKey(User.id), nullable=False)
    job_id = Column(UUID, ForeignKey(JobPost.id), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True))