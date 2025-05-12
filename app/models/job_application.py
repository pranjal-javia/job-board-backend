from sqlalchemy import Column, UUID, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from app.db import Base
from .user import User
from .job_post import JobPost

class JobApplication(Base):
    __tablename__ = "job_application"
    id = Column(UUID, primary_key=True)
    applicant_id = Column(UUID, ForeignKey(User.id), nullable=False)
    job_id = Column(UUID, ForeignKey(JobPost.id), nullable=False)
    user : Mapped["User"] = relationship(back_populates="job_applied")
    job_post : Mapped["JobPost"] = relationship(back_populates="job_applications") 
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True))