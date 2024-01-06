from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

import uuid
from ..base import AuditMixin, Base
from .enum import SeriesType
    

class DisciplineSeriesBase(Base, SQLModel):
    discipline: uuid.UUID = Field(foreign_key="discpline.id")
    series: int
    name: str
    type: SeriesType
    time: int
    number_of_shots: Optional[int]
    single_shots: Optional[bool]
    elimination: Optional[bool]
    shooters_to_eliminate: Optional[int]

class DisciplineSeries(DisciplineSeriesBase, SQLModel, table=True):
    __tablename__ = "discipline_series"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
  
class DisciplineSeriesCreate(DisciplineSeriesBase):
    pass

class DisciplineSeriesRead(DisciplineSeriesBase):
    id: uuid.UUID
