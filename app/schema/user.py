from pydantic import BaseModel, EmailStr

from app.models.user import UserTypeEnum, GenderEnum

class CreateUserInput(BaseModel):
    email: EmailStr
    password: str
    phone: str
    user_type: UserTypeEnum
    first_name: str
    middle_name: str = ""
    last_name: str
    gender: GenderEnum
