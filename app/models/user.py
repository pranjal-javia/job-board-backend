import enum
from typing import List, TYPE_CHECKING

from sqlalchemy import Column, UUID, String, ForeignKey, DateTime, func, Date, Enum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from app.db import Base

# to avoid circular import
# if TYPE_CHECKING:
#     from .job_post import JobPost
#     from .resume import Resume
#     from .job_application import JobApplication
#     from .saved_job import SavedJob
#     from .skill import Skill
#     from .experience import Experience
#     from .education import Education

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
    job_posted : Mapped[List["JobPost"]] = relationship(back_populates = "user")
    resume : Mapped["Resume"] = relationship(back_populates = "user")
    job_applied : Mapped[List["JobApplication"]] = relationship(back_populates = "user")
    saved_job : Mapped[List["SavedJob"]] = relationship(back_populates = "user")
    skills : Mapped[List["Skill"]] = relationship(back_populates = "user")
    experiences : Mapped[List["Experience"]] = relationship(back_populates = "user")
    educations : Mapped[List["Education"]] = relationship(back_populates = "user")
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True))

# to avoid circular dependency
from .job_post import JobPost
from .resume import Resume
from .job_application import JobApplication
from .saved_job import SavedJob
from .skill import Skill
from .experience import Experience
from .education import Education