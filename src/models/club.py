from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class ClubRequest(BaseModel):
    id: UUID
    name: str
    shortname: str
    country: int
