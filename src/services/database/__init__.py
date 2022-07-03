from settings import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .models import *  # noqa


settings = Settings()
engine = create_engine(settings.database_connection_uri, pool_pre_ping=True, future=True)  # echo=True to view sql queries in logs

DBSession: Session = sessionmaker(bind=engine, future=True)