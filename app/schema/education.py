from datetime import date

from pydantic import BaseModel, UUID4

class EducationOut(BaseModel):
    id: UUID4
    user_id: UUID4
    qualification: str
    grade_gained: str
    grade_total: str = ""
    start_at: date = None
    ended_at: date = None
    school_name: str

class EducationIn(BaseModel):
    user_id: UUID4
    qualification: str
    grade_gained: str
    grade_total: str = ""
    start_at: date = None
    ended_at: date = None
    school_name: str