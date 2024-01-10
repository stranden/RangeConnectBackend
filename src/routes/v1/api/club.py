import uuid
from typing import List
from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from services.database.crud import club as crud
from services.database.models import (
    ShootingClubCreate,
    ShootingClubRead
)

from ..dependencies import get_db

router = APIRouter()

@router.get("/", response_model=List[ShootingClubRead])
async def read_clubs(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Gets all clubs"""
    return crud.read_clubs(db, offset=offset, limit=limit)

@router.get("/{id}", response_model=ShootingClubRead)
async def read_club(id: uuid.UUID, db: Session = Depends(get_db)):
    """Gets specific club by ID"""
    db_club = crud.read_club(db, id)
    if db_club is None:
        raise HTTPException(status_code=404, detail="Club not found")
    return db_club
