from sqlmodel import SQLModel, MetaData, Field, Relationship
from typing import Optional, List

import uuid
from datetime import datetime
from decimal import Decimal
from enum import Enum

from .base import AuditMixin, Base

class SeriesType(Enum):
    SIGHT = "sight"
    MATCH = "match"
    SHOOTOFF = "shootoff"

class DisciplineStatus(Enum):
    DISABLED = "disabled"
    TESTING = "testing"
    ENABLED = "enabled"

class CompetitionStatus(Enum):
    CANCELLED = "cancelled"
    DELAYED = "delayed"
    FINISHED = "finished"
    PLANNED = "planned"
    STARTED = "started"

class EventStatus(Enum):
    CANCELLED = "cancelled"
    FINISHED = "finished"
    PLANNED = "planned"
    STARTED = "started"

### ------------------------------------------------
    
class LinkCompetitionRangeEventShooter(Base, table=True):
    __tablename__ = "link_competition_range_event_shooter"
    range_event_shooter_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, foreign_key="range_event_shooter.id", primary_key=True)
    competition_id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, foreign_key="competition.id", primary_key=True)

### ------------------------------------------------

class RangeEventShooterBase(AuditMixin, Base):

    firing_point: str
    start_number: str
    name: str
    club: Optional[str]
    group: Optional[str]

class RangeEventShooter(RangeEventShooterBase, table=True):
    __tablename__ = "range_event_shooter"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    shooting_range_id: uuid.UUID

    competitions: List["Competition"] = Relationship(back_populates="shooters", link_model=LinkCompetitionRangeEventShooter)

class RangeEventShooterCreate(RangeEventShooterBase):
    pass

class RangeEventShooterRead(RangeEventShooterBase):
    id: uuid.UUID

### ------------------------------------------------

class RangeEventShotBase(AuditMixin, Base):

    firing_point: str
    start_number: str
    series_type: SeriesType
    shot_id: int
    shot_value: Decimal
    shot_value_decimal: Decimal
    x_coord: Decimal
    y_coord: Decimal

class RangeEventShot(RangeEventShotBase, table=True):
    __tablename__ = "range_event_shot"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)

    shooting_range_id: uuid.UUID

class RangeEventShooterCreate(RangeEventShotBase):
    pass

class RangeEventShooterRead(RangeEventShotBase):
    id: uuid.UUID

### ------------------------------------------------
    
class CountryBase(Base):
    __tablename__ = "country"
    code: str
    name: str

class Country(CountryBase, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    
    shooting_club: "ShootingClub" = Relationship(back_populates="country")

class CountryCreate(CountryBase):
    pass

class CountryRead(CountryBase):
    id: uuid.UUID

### ------------------------------------------------

class ShootingClubBase(Base):
    name: str
    shortname: Optional[str]

class ShootingClub(ShootingClubBase, table=True):
    __tablename__ = "shooting_club"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)

    country_id: uuid.UUID = Field(foreign_key="country.id")
    country: Country = Relationship(back_populates="shooting_club")

    shooting_range: "ShootingRange" = Relationship(back_populates="shooting_club")
    event: "Event" = Relationship(back_populates="shooting_club")

class ShootingClubCreate(ShootingClubBase):
    pass

class ShootingClubRead(ShootingClubBase):
    id: uuid.UUID

### ------------------------------------------------

class RangeManufactorBase(Base):
    name: str

class RangeManufactor(RangeManufactorBase, table=True):
    __tablename__ = "range_manufactor"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    
    shooting_range: "ShootingRange" = Relationship(back_populates="range_manufactor")

class RangeManufactorCreate(RangeManufactorBase):
    pass

class RangeManufactorRead(RangeManufactorBase):
    id: uuid.UUID

### ------------------------------------------------

class ShootingRangeBase(Base):
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

    competition: Optional["Competition"] = Relationship(back_populates="shooting_range")
    

class ShootingRangeCreate(ShootingRangeBase):
    pass

class ShootingRangeRead(ShootingRangeBase):
    id: uuid.UUID

### ------------------------------------------------

class DisciplineBase(Base):
    name: str
    shortname: str
    status: DisciplineStatus

class Discipline(DisciplineBase, table=True):
    __tablename__ = "discipline"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
  
    series: List["DisciplineSeries"] = Relationship(back_populates="discipline")
    competition: "Competition" = Relationship(back_populates="discipline")

class DisciplineCreate(DisciplineBase):
    pass

class DisciplineRead(DisciplineBase):
    id: uuid.UUID

### ------------------------------------------------

class DisciplineSeriesBase(Base):
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
    discipline: Discipline = Relationship(back_populates="series")

class DisciplineSeriesCreate(DisciplineSeriesBase):
    pass

class DisciplineSeriesRead(DisciplineSeriesBase):
    id: uuid.UUID

### ------------------------------------------------
    
class EventBase(Base):
    name: str
    startdate: datetime
    enddate: Optional[datetime]
    status: EventStatus

class Event(EventBase, table=True):
    __tablename__ = "event"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
  
    shooting_club_id: uuid.UUID = Field(foreign_key="shooting_club.id")
    shooting_club: ShootingClub = Relationship(back_populates="event")

    competitions: List["Competition"] = Relationship(back_populates="event")

class EventCreate(EventBase):
    pass

class EventRead(EventBase):
    id: uuid.UUID

### ------------------------------------------------

class CompetitionBase(Base):
    name: str
    shortname: Optional[str]
    startdate: datetime
    enddate: Optional[datetime]
    status: CompetitionStatus

class Competition(CompetitionBase, table=True):
    __tablename__ = "competition"
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, index=True)

    event_id: uuid.UUID = Field(foreign_key="event.id")
    event: Event = Relationship(back_populates="competitions")

    discipline_id: uuid.UUID = Field(foreign_key="discipline.id")
    discipline: Discipline = Relationship(back_populates="competition")

    shooting_range_id: Optional[uuid.UUID] = Field(foreign_key="shooting_range.id")
    shooting_range: ShootingRange = Relationship(back_populates="competition")

    shooters: List[RangeEventShooter] = Relationship(back_populates="competitions", link_model=LinkCompetitionRangeEventShooter)

class CompetitionCreate(CompetitionBase):
    pass

class CompetitionRead(CompetitionBase):
    id: uuid.UUID
    discipline: Optional[Discipline] = None
    shooting_range: Optional[ShootingRange] = None

### ------------------------------------------------

class ShootingRangeReadWithShooters(ShootingRangeRead):
    shooters: Optional[RangeEventShooter] = None

class EventReadWithCompetitions(EventRead):
    competitions: List[CompetitionRead] = []

class DisciplineReadWithDisciplineSeries(DisciplineRead):
    series: List[DisciplineSeriesRead] = []

class CompetitionReadWithRangeEventShooters(CompetitionRead):
    shooters: List[RangeEventShooter] = []

class CompetitionReadWithRangeEventShootersAndRangeEventShots(CompetitionReadWithRangeEventShooters):
    shots: List[RangeEventShot] = []

