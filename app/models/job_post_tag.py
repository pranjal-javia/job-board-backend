from sqlalchemy import Column, UUID, String, ForeignKey, DateTime, func, Date, Enum, Integer, Date
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from app.db import Base
from .job_post import JobPost

class JobPostTag(Base):
    __tablename__ = "job_post_tag"
    id = Column(UUID, primary_key=True)
    job_post_id = Column(UUID, ForeignKey(JobPost.id), nullable=False)
    job_post : Mapped["JobPost"] = relationship(back_populates="job_post_tags")
    created_at = Column(DateTime(timezone=True), default=func.now())