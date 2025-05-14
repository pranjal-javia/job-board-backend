from pydantic import BaseModel, UUID4

class SkillIn(BaseModel):
    user_id: UUID4
    skill: str

class SkillOut(BaseModel):
    id: UUID4
    user_id: UUID4
    skill: str