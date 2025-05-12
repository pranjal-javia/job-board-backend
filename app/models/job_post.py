import enum
from typing import List, TYPE_CHECKING

from sqlalchemy import Column, UUID, String, ForeignKey, DateTime, func, Enum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from app.db import Base
from .user import User

class RecruitmentTagEnum(enum.Enum):
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
    job_applications : Mapped[List["JobApplication"]] = relationship(back_populates="job_post")
    job_post_tags : Mapped[List["JobPostTag"]] = relationship(back_populates="job_post")
    user : Mapped["User"] = relationship(back_populates="job_posted")
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True))

# to avoid circular dependency
from .job_application import JobApplication
from .job_post_tag import JobPostTag