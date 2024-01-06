from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

import uuid
from ..base import AuditMixin, Base
from .enum import CompetitionStatus
    

class CompetitionBase(Base, SQLModel):
    event: uuid.UUID
    discipline: uuid.UUID = Field(foreign_key="discpline.id")
    name: str
    shortname: Optional[str]
    startdate: int
    enddate: int
    status: CompetitionStatus

class Competition(CompetitionBase, SQLModel, table=True):
    __tablename__ = "competition"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
  
class CompetitionCreate(CompetitionBase):
    pass

class CompetitionRead(CompetitionBase):
    id: uuid.UUID
