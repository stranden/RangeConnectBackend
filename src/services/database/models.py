import uuid
from enum import Enum as PyEnum, unique

from sqlalchemy import (
    Boolean,
    Column,
    Enum,
    Float,
    ForeignKey,
    Integer,
    Sequence,
    String,
    Table,
    TIMESTAMP,
    func
)
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from .base import AuditMixin, Base

class SeriesType(PyEnum):
    SIGHT = "sight"
    MATCH = "match"
    SHOOTOFF = "shootoff"


class DisciplineStatus(PyEnum):
    DISABLED = "disabled"
    TESTING = "testing"
    ENABLED = "enabled"


class CompetitionStatus(PyEnum):
    DISABLED = "disabled"
    TESTING = "testing"
    ENABLED = "enabled"


class Country(Base):
    __tablename__ = "country"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)

    def __init__(self, code: str, name: str) -> None:
        self.code = code
        self.name = name


class ShootingClub(AuditMixin, Base):
    __tablename__ = "shooting_club"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    country = Column(postgresql.UUID(as_uuid=True), ForeignKey("country.id"), nullable=False, index=True)
    name = Column(String, unique=True)
    shortname = Column(String, unique=True)

    def __init__(self, country: uuid, name: str, shortname: str) -> None:
        self.country = country
        self.name = name
        self.shortname = shortname


class RangeManufactor(AuditMixin, Base):
    __tablename__ = "range_manufactor"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False)


class ShootingRange(Base):
    __tablename__ = "shooting_range"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    shooting_club = Column(postgresql.UUID(as_uuid=True), ForeignKey("shooting_club.id"), nullable=True, index=True)
    range_manufactor = Column(postgresql.UUID(as_uuid=True), ForeignKey("range_manufactor.id"), nullable=False, index=True)
    name = Column(String, nullable=False)
    lanes = Column(Integer, nullable=False)
    first_lane = Column(String, nullable=False)


class Event(Base):
    __tablename__ = "event"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    shooting_club = Column(postgresql.UUID(as_uuid=True), ForeignKey("shooting_club.id"), nullable=True, index=True)
    name = Column(String, nullable=False)
    startdate = Column(TIMESTAMP, nullable=False)
    enddate = Column(TIMESTAMP, nullable=False)
    status = Column(Integer, nullable=False, default=0)


class EventRange(Base):
    __tablename__ = "event_range"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    event = Column(postgresql.UUID(as_uuid=True), ForeignKey("event.id"), nullable=False, index=True)
    shooting_range = Column(postgresql.UUID(as_uuid=True), ForeignKey("shooting_range.id"), nullable=False, index=True)


class Dicipline(Base):
    __tablename__ = "dicipline"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    shortname = Column(String, unique=True)
    status = Column(Enum(DisciplineStatus), nullable=False)


class DiciplineSeries(Base):
    __tablename__ = "dicipline_series"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    discipline = Column(postgresql.UUID(as_uuid=True), ForeignKey("discipline.id"), nullable=False, index=True)
    series = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    type = Column(Enum(SeriesType), nullable=False)
    time = Column(Integer, nullable=False)
    number_of_shots = Column(Integer, nullable=True)
    single_shots = Column(Boolean, nullable=True)
    elimination = Column(Boolean, nullable=True)
    shooters_to_eliminate = Column(Integer, nullable=True)


class Competition(Base):
    __tablename__ = "competition"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    event = Column(postgresql.UUID(as_uuid=True), ForeignKey("event.id"), nullable=False, index=True)
    discipline = Column(postgresql.UUID(as_uuid=True), ForeignKey("discipline.id"), nullable=False, index=True)
    name = Column(String, nullable=False)
    shortname = Column(String, unique=False)
    startdate = Column(TIMESTAMP, nullable=False)
    enddate = Column(TIMESTAMP, nullable=False)
    status = Column(Enum(CompetitionStatus), nullable=False)

