from sqlalchemy import Column, UUID, String, ForeignKey, DateTime, func, Date, Enum

from app.db import Base
from .user import User

class Session(Base):
    __tablename__ = "session"
    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, ForeignKey(User.id), nullable=False)
    jwt_token = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True))