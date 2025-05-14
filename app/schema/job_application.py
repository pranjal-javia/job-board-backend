from pydantic import BaseModel, UUID4, EmailStr

from .job_post import JobPostOut
from .resume import ResumeOut

class JobApplicationIn(BaseModel):
    applicant_id: UUID4
    job_id: UUID4

class JobPostOut_for_JobApplication(BaseModel):
    id: UUID4
    recruiter_id: UUID4
    company_name: str
    company_mail: EmailStr
    contact_number: str
    role: str
    location: str
    employement_type: str
    description: str = ""
    recruitment_tag: str 

class JobApplicationOut(BaseModel):
    id: UUID4
    applicant_id: UUID4
    job_post: JobPostOut
    resume: ResumeOut