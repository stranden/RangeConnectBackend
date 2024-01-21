import uuid
from typing import List
from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from services.database.crud import event as crud
from services.database.models import (
    EventCreate,
    EventRead,
    EventReadWithCompetitions,
    Event
)

from ..dependencies import get_db

router = APIRouter()

@router.get("/", response_model=List[EventReadWithCompetitions])
async def read_events(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all events"""
    return crud.read_events(db, offset=offset, limit=limit)

@router.get("/{id}", response_model=EventReadWithCompetitions)
async def read_event(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get specific event by ID"""
    db_event = crud.read_event(db, id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


#@router.get("/")
#async def event():
#    return {"message": "GET All events"}
#
#@router.get("/{event_id}")
#async def event_by_id(event_id):
#    return {"message": "GET specific event with ID", "event": event_id}
#
#@router.get("/{event_id}/competition")
#async def event_by_id_competition(event_id):
#    return {"message": "GET All competitions from specific event with ID", "event": event_id}
#
#@router.get("/{event_id}/competition/{competition_id}")
#async def event_by_id_competition_by_id(event_id, competition_id):
#    return {"message": "GET All competitions from specific event with ID", "event": event_id, "competition": competition_id}
#