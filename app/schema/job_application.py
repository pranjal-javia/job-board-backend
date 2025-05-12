from pydantic import BaseModel

class JobApplicationIn(BaseModel):
    applicant_id: str
    job_id: str

class JobApplicatioOut(BaseModel):
    id: str
    applicant_id: str
    job_id: str