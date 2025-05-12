from sqlalchemy import Column, UUID, String, ForeignKey, DateTime, func, Date, Enum, Integer, Date
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from app.db import Base
from .user import User

class Education(Base):
    __tablename__ = "education"
    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, ForeignKey(User.id), nullable=False)
    qualification = Column(String, nullable=False)
    grade_gained = Column(String, nullable=False)
    grade_total = Column(String, nullable=True)
    start_at = Column(Date, nullable=True)
    ended_at = Column(Date, nullable=True)
    school_name = Column(String, nullable=False)
    user : Mapped["User"] = relationship(back_populates="educations") 
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True))