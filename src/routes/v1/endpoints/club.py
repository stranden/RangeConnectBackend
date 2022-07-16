import uuid
from http import HTTPStatus
from typing import List, Optional

from fastapi import APIRouter, Depends, Response
from fastapi.exceptions import HTTPException
from models.club import (
    ClubRequest
)

router = APIRouter()

@router.get("/", response_model=ClubRequest)
async def club():
    return {"message": "GET All clubs"}

@router.get("/{club_id}")
async def club_by_id(club_id):
    return {"message": "GET specific club with ID", "club": club_id}