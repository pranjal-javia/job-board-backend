import enum

from sqlalchemy import Column, UUID, String, ForeignKey, DateTime, func, Date, Enum

from app.db import Base

class UserTypeEnum(enum.Enum):
    applicant = "applicant"
    recruiter = "recruiter"

class GenderEnum(enum.Enum):
    male = "male"
    female = "female"
    other = "other"

class User(Base):
    __tablename__ = "user"
    id = Column(UUID, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    phone = Column(String, nullable=False)
    user_type = Column(Enum(UserTypeEnum, name="usertypeenum", create_type=False), nullable=False)
    gender = Column(Enum(GenderEnum, name="gendertypeenum", creat_type=False), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True))