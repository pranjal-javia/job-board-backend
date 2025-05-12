from sqlalchemy import Column, UUID, String, ForeignKey, DateTime, func, Date, Enum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from app.db import Base
from .user import User
from .job_post import JobPost

class SavedJob(Base):
    __tablename__ = "saved_job"
    id = Column(UUID, primary_key=True)
    applicant_id = Column(UUID, ForeignKey(User.id), nullable=False)
    job_id = Column(UUID, ForeignKey(JobPost.id), nullable=False)
    user : Mapped["User"] = relationship(back_populates="saved_job")
    created_at = Column(DateTime(timezone=True), default=func.now())