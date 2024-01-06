from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

import uuid
from ..base import AuditMixin, Base
from .country import Country
    

class ShootingClubBase(Base, SQLModel):
    name: str
    shortname: str

class ShootingClub(ShootingClubBase, SQLModel, table=True):
    __tablename__ = "shooting_club"

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)

    country_id: uuid.UUID = Field(foreign_key="country.id")
    
class ShootingClubCreate(ShootingClubBase):
    pass

class ShootingClubRead(ShootingClubBase):
    id: uuid.UUID
