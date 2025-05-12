import uuid
import bcrypt

from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.schema.user import CreateUserInput
from app.models.user import User

router = APIRouter()

def password_hasing(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


# for getting use by email id, required query parameter used
# @router.get("/user/")
# async def get_user_by_email(email: str, password: str):
#     return "user by email id"

# for creating user
@router.post("/user", status_code=status.HTTP_201_CREATED)
async def crete_user(user_data: CreateUserInput, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.email == user_data.email).first()
        if user:
            raise HTTPException(
                status_code = 422,
                detail = "User already exist" 
            )
        else:
            hashed_password = password_hasing(user_data.password)
            new_user = User(
                id = uuid.uuid4(),
                email = user_data.email,
                password = hashed_password,
                phone = user_data.phone,
                user_type = user_data.user_type,
                first_name = user_data.first_name,
                last_name = user_data.last_name,
                middle_name = user_data.middle_name,
                gender = user_data.gender
            )
            db.add(new_user)
            db.commit()
    except Exception as e:
        print(f"error occured : {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating user: {e}"
        )