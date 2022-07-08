from functools import lru_cache

from fastapi import Depends
from services.database import DBSession
from settings import Settings
from sqlalchemy.orm.session import Session


@lru_cache()
def get_settings():
    return Settings()


def get_db() -> Session:
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
