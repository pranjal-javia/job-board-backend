from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.user import User
from app.schema.user import UserOut

router = APIRouter()

@router.get("/auth/login", response_model=UserOut)
async def get_user_by_email(email: str, password: str | None = None, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.email == email).first()
        print(user.email)
        print(user.password)
        # user = db.query(User).all()
        # user.password = ""
        return user
    except Exception as e:
        print(f"error occured : {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while fetching the user: {e}"
        )