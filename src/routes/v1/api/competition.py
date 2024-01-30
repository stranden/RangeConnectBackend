import uuid
from typing import List
from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from services.database.crud import competition as crud
from services.database.models import (
    CompetitionCreate,
    CompetitionRead,
    CompetitionReadWithRangeEventShooters,
    CompetitionReadWithRangeEventShootersAndRangeEventShots,
    Competition
)

from ..dependencies import get_db

router = APIRouter()


@router.get("/", response_model=List[CompetitionReadWithRangeEventShooters])
async def read_competitions(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all competitions"""
    return crud.read_competitions(db, offset=offset, limit=limit)

@router.get("/{id}", response_model=CompetitionReadWithRangeEventShooters)
async def read_competition(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get specific competition by ID"""
    db_competition = crud.read_competition(db, id)
    if db_competition is None:
        raise HTTPException(status_code=404, detail="Competition not found")
    return db_competition

@router.get("/{id}/shots", response_model=CompetitionReadWithRangeEventShootersAndRangeEventShots)
async def read_competition_shots(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get specific competition by ID"""
    db_competition = crud.read_competition(db, id)
    if db_competition is None:
        raise HTTPException(status_code=404, detail="Competition not found")
    return db_competition
