from sqlalchemy import Column, UUID, String, ForeignKey, DateTime, func, Date, Enum, Integer, Date

from app.db import Base
from .user import User

class ForgetPassword(Base):
    __tablename__ = "forget_password"
    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, ForeignKey(User.id), nullable=False)
    otp = Column(String, nullable=False)