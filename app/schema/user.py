from typing import List, Optional

from pydantic import BaseModel, EmailStr, UUID4

from app.models.user import UserTypeEnum, GenderEnum
from .job_post import JobPostOut
from .resume import ResumeOut
from .skill import SkillOut
from .experience import ExperienceOut
from .education import EducationOut
from .job_post import JobPostOut
from .job_application import JobApplicationOut

class CreateUserInput(BaseModel):
    email: EmailStr
    password: str
    phone: str
    user_type: UserTypeEnum
    first_name: str
    middle_name: str = ""
    last_name: str
    gender: GenderEnum

# class JobApplied(BaseModel):
#     applicant_id: UUID4
#     company_name: str
#     company_mail: EmailStr
#     contact_number: str
#     role: str
#     location: str
#     employment_type: str
#     resume: ResumeOut

class UserOut(BaseModel):
    id: UUID4
    email: EmailStr
    first_name: str
    last_name: str
    middle_name: str
    phone: str
    user_type: UserTypeEnum
    gender: GenderEnum
    job_posted: List[JobPostOut]
    job_applied: List[JobApplicationOut]
    saved_job: Optional[List[JobPostOut]] = None
    skills: List[SkillOut] = None
    experiences: List[ExperienceOut] = None
    educations: List[EducationOut] = None