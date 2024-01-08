import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from services.database.crud import club as crud
from services.database.models import (
    ShootingClubCreate,
    ShootingClubRead
)

from ..dependencies import get_db

router = APIRouter()

@router.get("/{id}", response_model=ShootingClubRead)
async def read_club(id: uuid.UUID, db: Session = Depends(get_db)):
    """Gets specific club by ID"""
    db_club = crud.read_club(db, id)
    if db_club is None:
        raise HTTPException(status_code=404, detail="Club not found")
    return db_club

@router.get("/", response_model=List[ShootingClubRead])
async def read_club(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Gets all clubs"""
    return crud.read_clubs(db, offset=offset, limit=limit)

#@router.get("/", response_model=List[ShootingClubRead])
#async def get_clubs(db: Session = Depends(get_db)):
#    """Gets all clubs"""
#    clubs = db.exec(select(ShootingClubRead)).all()
#    return clubs
#
#@router.get("/{club_id}")
#async def get_club_by_id(club_id: int, db: Session = Depends(get_db)):
#    """Gets specific club by ID"""
#    club = db.get(ShootingClubRead, club_id)
#    if not club:
#        return {"message": "Club not found"}
#    return club.model_dump()
