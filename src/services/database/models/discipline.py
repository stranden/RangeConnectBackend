from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

import uuid
from ..base import AuditMixin, Base
from .enum import DisciplineStatus
    

class DisciplineBase(Base, SQLModel):
    name: str
    shortname: str
    status: DisciplineStatus

class Discipline(DisciplineBase, SQLModel, table=True):
    __tablename__ = "discipline"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
  
class DisciplineCreate(DisciplineBase):
    pass

class DisciplineRead(DisciplineBase):
    id: uuid.UUID
