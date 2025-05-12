from sqlalchemy import Column, UUID, String, ForeignKey, DateTime, func, Date, Enum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from app.db import Base
from .user import User

class Skill(Base):
    __tablename__ = "skill"
    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, ForeignKey(User.id), nullable=False)
    skill = Column(String, nullable=False)
    user : Mapped["User"] = relationship(back_populates="skills")
    created_at = Column(DateTime(timezone=True), default=func.now())