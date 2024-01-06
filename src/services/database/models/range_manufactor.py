from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

import uuid
from ..base import AuditMixin, Base
    

class RangeManufactorBase(Base, SQLModel):
    name: str

class RangeManufactor(RangeManufactorBase, SQLModel, table=True):
    __tablename__ = "range_manufactor"

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    
class RangeManufactorCreate(RangeManufactorBase):
    pass

class RangeManufactorRead(RangeManufactorBase):
    id: uuid.UUID

