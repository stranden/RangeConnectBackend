from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from services.database.models import (
    ShootingClubCreate,
    ShootingClubRead
)

from ..dependencies import get_db

router = APIRouter()

@router.get("/", response_model=List[ShootingClubRead])
#@router.get("/")
async def get_clubs(db: Session = Depends(get_db)):
    """Gets all clubs"""
    clubs = db.exec(select(ShootingClubRead)).all()
    return clubs

@router.get("/{club_id}")
async def get_club_by_id(club_id: int, db: Session = Depends(get_db)):
    """Gets specific club by ID"""
    club = db.get(ShootingClubRead, club_id)
    if not club:
        return {"message": "Club not found"}
    return club.model_dump()
