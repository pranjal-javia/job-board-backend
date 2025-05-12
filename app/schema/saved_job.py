from pydantic import BaseModel

class SavedJobIn(BaseModel):
    applicant_id: str
    job_id: str

class SavedJobOut(BaseModel):
    id: str
    applicant_id: str
    job_id: str