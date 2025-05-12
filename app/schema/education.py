from datetime import date

from pydantic import BaseModel

class EducationOut(BaseModel):
    id: str
    user_id: str
    qualification: str
    grade_gained: str
    grade_total: str
    start_at: date
    ended_at: date
    school_name: str

class EducationIn(BaseModel):
    user_id: str
    qualification: str
    grade_gained: str
    grade_total: str = ""
    start_at: date = None
    ended_at: date = None
    school_name: str