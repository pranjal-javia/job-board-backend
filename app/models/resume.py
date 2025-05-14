from sqlalchemy import Column, UUID, String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from app.db import Base
from .user import User
from .job_application import JobApplication

class Resume(Base):
    __tablename__ = "resume"
    id = Column(UUID, primary_key=True)
    applicant_id = Column(UUID, ForeignKey(User.id), nullable=False)
    job_application_id = Column(UUID, ForeignKey(JobApplication.id))
    resume_url = Column(String, nullable=False)
    job_application: Mapped["JobApplication"] = relationship(back_populates="resume")
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True))