from pydantic import BaseModel, EmailStr

class JobPostIn(BaseModel):
    recruiter_id: str
    company_name: str
    company_email: EmailStr
    contact_number: str
    role: str
    location: str
    employmet_type: str
    description: str = ""
    recruitment_tag: str

class JobPostOut(BaseModel):
    id: str
    recruiter_id: str
    company_name: str
    company_email: EmailStr
    contact_number: str
    role: str
    location: str
    employmet_type: str
    description: str = ""
    recruitment_tag: str