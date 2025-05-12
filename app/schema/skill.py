from pydantic import BaseModel

class SkillIn(BaseModel):
    user_id: str
    skill: str

class SkillOut(BaseModel):
    id: str
    user_id: str
    skill: str