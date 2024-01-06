from enum import Enum

class SeriesType(Enum):
    SIGHT = "sight"
    MATCH = "match"
    SHOOTOFF = "shootoff"

class DisciplineStatus(Enum):
    DISABLED = "disabled"
    TESTING = "testing"
    ENABLED = "enabled"

class CompetitionStatus(Enum):
    DISABLED = "disabled"
    TESTING = "testing"
    ENABLED = "enabled"

class EventStatus(Enum):
    CANCELLED = "cancelled"
    FINISHED = "finished"
    PLANNED = "planned"
    STARTED = "started"
    