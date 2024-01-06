from sqlmodel import Field, SQLModel
from typing import Optional

import uuid
from ..base import AuditMixin, Base

class CountryBase(Base, SQLModel):
    code: str
    name: str

class Country(CountryBase, SQLModel, table=True):
    __tablename__ = "country"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    
class CountryCreate(CountryBase):
    pass

class CountryRead(CountryBase):
    id: uuid.UUID