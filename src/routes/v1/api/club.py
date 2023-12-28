import uuid
from http import HTTPStatus
from typing import List, Optional

from fastapi import APIRouter, Depends, Response
from fastapi.exceptions import HTTPException
from models.club import (
    ClubRequest
)
from services.database import models
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session

from ..dependencies import get_db

router = APIRouter()

@router.get("/", response_model=List[ClubRequest])
async def club(db: Session = Depends(get_db)):
    """Gets all clubs
    """
    clubs: List[models.ShootingClub] = (db.query(models.ShootingClub)
                               .all())

    if not clubs:
        return []

    return clubs

@router.get("/{club_id}")
async def club_by_id(club_id):
    return {"message": "GET specific club with ID", "club": club_id}
    