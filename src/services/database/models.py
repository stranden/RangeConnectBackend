from sqlmodel import Field, Relationship, ForeignKey, SQLModel
from typing import Optional

import uuid
from .base import Base
from .shared.enum import (
    CompetitionStatus,
    DisciplineStatus,
    EventStatus,
    SeriesType
)

class EventRangeLink(Base, SQLModel, table=True):
    __tablename__ = "event_range_link"
    event_id: uuid.UUID = Field(foreign_key="event.id", primary_key=True)
    shooting_range_id: uuid.UUID = Field(foreign_key="shooting_range.id", primary_key=True)


 
class CountryBase(Base, SQLModel):
    code: str
    name: str

class Country(CountryBase, table=True):
    __tablename__ = "country"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    
class CountryCreate(CountryBase):
    pass

class CountryRead(CountryBase):
    id: uuid.UUID



class ShootingClubBase(Base, SQLModel):
    name: str
    shortname: str

class ShootingClub(ShootingClubBase, table=True):
    __tablename__ = "shooting_club"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)

    country_id: uuid.UUID = Field(foreign_key="country.id")
    country: Country = Relationship(back_populates="shooting_club")
    
class ShootingClubCreate(ShootingClubBase):
    pass

class ShootingClubRead(ShootingClubBase):
    id: uuid.UUID



class RangeManufactorBase(Base, SQLModel):
    name: str

class RangeManufactor(RangeManufactorBase, table=True):
    __tablename__ = "range_manufactor"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    
class RangeManufactorCreate(RangeManufactorBase):
    pass

class RangeManufactorRead(RangeManufactorBase):
    id: uuid.UUID



class ShootingRangeBase(Base, SQLModel):
    name: str
    lanes: int
    first_lane: str

class ShootingRange(ShootingRangeBase, table=True):
    __tablename__ = "shooting_range"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)

    shooting_club_id: uuid.UUID = Field(foreign_key="shooting_club.id")
    shooting_club: ShootingClub = Relationship(back_populates="shooting_range")

    range_manufactor_id: uuid.UUID = Field(foreign_key="range_manufactor.id")
    range_manufactor: RangeManufactor = Relationship(back_populates="shooting_range")

class ShootingRangeCreate(ShootingRangeBase):
    pass

class ShootingRangeRead(ShootingRangeBase):
    id: uuid.UUID



class DisciplineBase(Base, SQLModel):
    name: str
    shortname: str
    status: DisciplineStatus

class Discipline(DisciplineBase, table=True):
    __tablename__ = "discipline"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
  
class DisciplineCreate(DisciplineBase):
    pass

class DisciplineRead(DisciplineBase):
    id: uuid.UUID



class DisciplineSeriesBase(Base, SQLModel):
    series: int
    name: str
    type: SeriesType
    time: int
    number_of_shots: Optional[int]
    single_shots: Optional[bool]
    elimination: Optional[bool]
    shooters_to_eliminate: Optional[int]

class DisciplineSeries(DisciplineSeriesBase, table=True):
    __tablename__ = "discipline_series"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)

    discipline_id: uuid.UUID = Field(foreign_key="discipline.id")
    discipline: Discipline = Relationship(back_populates="discipline_series")

class DisciplineSeriesCreate(DisciplineSeriesBase):
    pass

class DisciplineSeriesRead(DisciplineSeriesBase):
    id: uuid.UUID


    
class EventBase(Base, SQLModel):
    name: str
    startdate: int
    enddate: int
    status: EventStatus

class Event(EventBase, table=True):
    __tablename__ = "event"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
  
    shooting_club_id: uuid.UUID = Field(foreign_key="shooting_club.id")
    shooting_club: ShootingClub = Relationship(back_populates="event")

class EventCreate(EventBase):
    pass

class EventRead(EventBase):
    id: uuid.UUID



class CompetitionBase(Base, SQLModel):
    event: uuid.UUID
    name: str
    shortname: Optional[str]
    startdate: int
    enddate: int
    status: CompetitionStatus

class Competition(CompetitionBase, table=True):
    __tablename__ = "competition"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)

    discipline_id: uuid.UUID = Field(foreign_key="discipline.id")
    discipline: Discipline = Relationship(back_populates="competition")
    
class CompetitionCreate(CompetitionBase):
    pass

class CompetitionRead(CompetitionBase):
    id: uuid.UUID