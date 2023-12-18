from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class ClubRequest(BaseModel):
    id: UUID
    country: UUID
    name: str
    shortname: str
    
    class Config:
        orm_mode = True