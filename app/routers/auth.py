from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.user import User

router = APIRouter()

@router.get("/auth/login")
async def get_user_by_email(email: str, password: str, db: Session = Depends(get_db)):
    try:
        # user = db.query(User).filter(User.email == email).all()
        user = db.query(User).all()
        # user.password = ""
        return user
    except Exception as e:
        print(f"error occured : {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while fetching the user: {e}"
        )