from sqlmodel import SQLModel, MetaData, Field
from settings import Settings
from datetime import datetime

settings = Settings()

class Base(SQLModel, table=False):
    metadata = MetaData(schema=settings.DATABASE_SCHEMA)

class AuditMixin(SQLModel):
    created_date: datetime = Field(default_factory=datetime.utcnow)
    modified_date: datetime = Field(default_factory=datetime.utcnow)