from sqlmodel import Field, SQLModel
from typing import Optional

import uuid
from .base import AuditMixin, Base











class ShootingRange(Base, SQLModel):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    shooting_club: Optional[uuid.UUID]
    range_manufactor: uuid.UUID
    name: str
    lanes: int
    first_lane: str


class Event(Base, SQLModel):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    shooting_club: Optional[uuid.UUID]
    name: str
    startdate: int
    enddate: int
    status: int = 0


class EventRange(Base, SQLModel):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    event: uuid.UUID
    shooting_range: uuid.UUID


class Dicipline(Base, SQLModel):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    name: str
    shortname: str
    status: DisciplineStatus


class DiciplineSeries(Base, SQLModel):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    discipline: uuid.UUID
    series: int
    name: str
    type: SeriesType
    time: int
    number_of_shots: Optional[int]
    single_shots: Optional[bool]
    elimination: Optional[bool]
    shooters_to_eliminate: Optional[int]


class Competition(Base, SQLModel):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    event: uuid.UUID
    discipline: uuid.UUID
    name: str
    shortname: Optional[str]
    startdate: int
    enddate: int
    status: CompetitionStatus
