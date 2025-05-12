from pydantic import BaseModel

class ResumeIn(BaseModel):
    application_id: str
    resume_url: str

class ResumeOut(BaseModel):
    id: str
    application_id: str
    resume_url: str