from functools import lru_cache

from fastapi import Depends
from services.database import engine
from settings import Settings
from sqlmodel import Session


@lru_cache()
def get_settings():
    return Settings()


def get_db():
    with Session(engine) as session:
        yield session
