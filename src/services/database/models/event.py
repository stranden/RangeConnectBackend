from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

import uuid
from ..base import AuditMixin, Base
from .enum import EventStatus
    

class EventBase(Base, SQLModel):
    shooting_club: uuid.UUID = Field(foreign_key="shooting_club.id")
    name: str
    startdate: int
    enddate: int
    status: EventStatus

class Event(EventBase, SQLModel, table=True):
    __tablename__ = "event"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
  
class EventCreate(EventBase):
    pass

class EventRead(EventBase):
    id: uuid.UUID
