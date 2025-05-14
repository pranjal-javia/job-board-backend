from pydantic import BaseModel, UUID4

class ExperienceIn(BaseModel):
    user_id: UUID4
    year: int
    company_name: str

class ExperienceOut(BaseModel):
    id: UUID4
    user_id: UUID4
    year: int
    company_name: str