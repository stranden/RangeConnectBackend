import uuid
from http import HTTPStatus
from typing import List, Optional

from fastapi import APIRouter, Depends, Response
from fastapi.exceptions import HTTPException


router = APIRouter()

@router.get("/")
async def event():
    return {"message": "GET All events"}

@router.get("/{event_id}")
async def event_by_id(event_id):
    return {"message": "GET specific event with ID", "event": event_id}

@router.get("/{event_id}/competition")
async def event_by_id_competition(event_id):
    return {"message": "GET All competitions from specific event with ID", "event": event_id}

@router.get("/{event_id}/competition/{competition_id}")
async def event_by_id_competition_by_id(event_id, competition_id):
    return {"message": "GET All competitions from specific event with ID", "event": event_id, "competition": competition_id}