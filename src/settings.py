import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", default="localhost")
    DATABASE_USER: str = os.getenv("DATABASE_USER", default="rangeconnect")
    DATABASE_PASS: str = os.getenv("DATABASE_PASS", default="MzqGbe#o8AUn")
    DATABASE_DB: str = os.getenv("DATABASE_DB", default="rangeconnect")
    DATABASE_SCHEMA: str = os.getenv("DATABASE_SCHEMA", default="rangeconnect")
    DATABASE_URI: str = f"postgresql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}/{DATABASE_DB}"