from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

from sqlalchemy.orm import DeclarativeBase

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()