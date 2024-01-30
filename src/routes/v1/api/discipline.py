import uuid
from typing import List
from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from services.database.crud import discipline as crud
from services.database.models import (
    DisciplineCreate,
    DisciplineRead,
    DisciplineReadWithDisciplineSeries,
    Discipline
)

from ..dependencies import get_db

router = APIRouter()

@router.get("/", response_model=List[DisciplineReadWithDisciplineSeries])
async def read_disciplines(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all disciplines"""
    return crud.read_disciplines(db, offset=offset, limit=limit)

@router.get("/{id}", response_model=DisciplineReadWithDisciplineSeries)
async def read_discipline(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get specific discipline by ID"""
    db_discipline = crud.read_discipline(db, id)
    if db_discipline is None:
        raise HTTPException(status_code=404, detail="Discipline not found")
    return db_discipline


#@router.get("/")
#async def discipline():
#    return {"message": "GET All disciplines"}
#
#@router.get("/{discipline_id}")
#async def discipline_by_id(discipline_id):
#    return {"message": "GET specific discipline with ID", "discipline": discipline_id}
#
#@router.get("/{discipline_id}/competition")
#async def discipline_by_id_competition(discipline_id):
#    return {"message": "GET All competitions from specific discipline with ID", "discipline": discipline_id}
#
#@router.get("/{discipline_id}/competition/{competition_id}")
#async def discipline_by_id_competition_by_id(discipline_id, competition_id):
#    return {"message": "GET All competitions from specific discipline with ID", "discipline": discipline_id, "competition": competition_id}
#