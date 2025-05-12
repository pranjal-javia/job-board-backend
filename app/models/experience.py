from sqlalchemy import Column, UUID, String, ForeignKey, DateTime, func, Date, Enum, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from app.db import Base
from .user import User

class Experience(Base):
    __tablename__ = "experience"
    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, ForeignKey(User.id), nullable=False)
    year = Column(Integer, nullable=False)
    company_name = Column(String, nullable=False)
    user : Mapped["User"] = relationship(back_populates="experiences")
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True))