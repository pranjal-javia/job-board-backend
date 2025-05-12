from pydantic import BaseModel

class ExperienceIn(BaseModel):
    user_id: str
    year: int
    company_name: str

class ExperienceOut(BaseModel):
    id: str
    user_id: str
    year: int
    company_name: str