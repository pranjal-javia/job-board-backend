# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"  # points to your root-level .env file

# Singleton instance
settings = Settings()
