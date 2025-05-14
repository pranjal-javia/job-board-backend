from pydantic import BaseModel, EmailStr, UUID4

class JobPostIn(BaseModel):
    recruiter_id: UUID4
    company_name: str
    company_email: EmailStr
    contact_number: str
    role: str
    location: str
    employmet_type: str
    description: str = ""
    recruitment_tag: str

class JobPostOut(BaseModel):
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