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
    Competition
)

from ..dependencies import get_db

router = APIRouter()


@router.get("/", response_model=List[CompetitionRead])
async def read_competitions(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all competitions"""
    return crud.read_competitions(db, offset=offset, limit=limit)

@router.get("/{id}", response_model=CompetitionRead)
async def read_competition(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get specific competition by ID"""
    db_competition = crud.read_competition(db, id)
    if db_competition is None:
        raise HTTPException(status_code=404, detail="Competition not found")
    return db_competition


#@router.get("/")
#async def competition():
#    return {"message": "GET All competitions"}
#
#@router.get("/{competition_id}")
#async def competition_by_id(competition_id):
#    return {"message": "GET specific competition with ID", "competition": competition_id}
#
#@router.get("/{competition_id}/competition")
#async def competition_by_id_competition(competition_id):
#    return {"message": "GET All competitions from specific competition with ID", "competition": competition_id}
#
#@router.get("/{competition_id}/competition/{competition_id}")
#async def competition_by_id_competition_by_id(competition_id, competition_id):
#    return {"message": "GET All competitions from specific competition with ID", "competition": competition_id, "competition": competition_id}
#