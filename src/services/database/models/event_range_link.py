from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

import uuid
from ..base import AuditMixin, Base
    

class EventRangeLinkBase(Base, SQLModel):
    shooting_club: uuid.UUID = Field(foreign_key="shooting_club.id")


class EventRangeLink(EventRangeLinkBase, SQLModel, table=True):
    __tablename__ = "event_range_link"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
  
class EventCreate(EventBase):
    pass

class EventRead(EventBase):
    id: uuid.UUID



class EventRange(Base, SQLModel):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    event: uuid.UUID
    shooting_range: uuid.UUID


class HeroTeamLink(SQLModel, table=True):
    team_id: Optional[int] = Field(
        default=None, foreign_key="team.id", primary_key=True
    )
    hero_id: Optional[int] = Field(
        default=None, foreign_key="hero.id", primary_key=True
    )