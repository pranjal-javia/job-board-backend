from pydantic import BaseModel, UUID4

class ResumeIn(BaseModel):
    job_post_id: UUID4
    applicant_id: UUID4
    resume_url: str

class ResumeOut(BaseModel):
    id: UUID4
    job_application_id: UUID4
    applicant_id: UUID4
    resume_url: str