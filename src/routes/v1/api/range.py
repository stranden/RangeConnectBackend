import uuid
from typing import List
from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from services.database.crud import range as crud
from services.database.models import (
    ShootingRangeCreate,
    ShootingRangeRead
)

from ..dependencies import get_db

router = APIRouter()

@router.get("/", response_model=List[ShootingRangeRead])
async def read_shooting_ranges(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Gets all ranges"""
    return crud.read_shooting_ranges(db, offset=offset, limit=limit)

@router.get("/{id}", response_model=ShootingRangeRead)
async def read_shooting_range(id: uuid.UUID, db: Session = Depends(get_db)):
    """Gets specific range by ID"""
    db_shooting_range = crud.read_shooting_range(db, id)
    if db_shooting_range is None:
        raise HTTPException(status_code=404, detail="Range not found")
    return db_shooting_range
