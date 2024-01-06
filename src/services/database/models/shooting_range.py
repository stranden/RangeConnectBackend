from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

import uuid
from ..base import AuditMixin, Base
    

class ShootingRangeBase(Base, SQLModel):
    name: str
    lanes: int
    first_lane: str

class ShootingRange(ShootingRangeBase, SQLModel, table=True):
    __tablename__ = "shooting_range"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)

    shooting_club: uuid.UUID = Field(foreign_key="shooting_club.id")
    range_manufactor: uuid.UUID = Field(foreign_key="range_manufactor.id")
    
class ShootingRangeCreate(ShootingRangeBase):
    pass

class ShootingRangeRead(ShootingRangeBase):
    id: uuid.UUID
