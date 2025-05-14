from pydantic import BaseModel, UUID4

class SavedJobIn(BaseModel):
    applicant_id: UUID4
    job_id: UUID4

class SavedJobOut(BaseModel):
    id: UUID4
    applicant_id: UUID4
    job_id: UUID4