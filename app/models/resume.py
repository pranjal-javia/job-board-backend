from sqlalchemy import Column, UUID, String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from app.db import Base
from .user import User

class Resume(Base):
    __tablename__ = "resume"
    id = Column(UUID, primary_key=True)
    applicant_id = Column(UUID, ForeignKey(User.id), nullable=False)
    resume_url = Column(String, nullable=False)
    user : Mapped["User"] = relationship(back_populates="resume")
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True))