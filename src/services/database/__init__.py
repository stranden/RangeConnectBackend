from settings import Settings
from sqlmodel import create_engine, Session

from services.database.models import *  # noqa

settings = Settings()

# Create a SQLModel-compatible engine
engine = create_engine(settings.DATABASE_URI, pool_pre_ping=True, echo=True)
