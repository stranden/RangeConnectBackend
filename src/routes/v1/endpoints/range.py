import uuid
from http import HTTPStatus
from typing import List, Optional

from fastapi import APIRouter, Depends, Response
from fastapi.exceptions import HTTPException
#from models.club import (
#    ClubRequest
#)

router = APIRouter()

@router.get("/")
async def range():
    return {"message": "GET All ranges"}

@router.get("/{range_id}")
async def range_by_id(range_id):
    return {"message": "GET specific range with ID", "range": range_id}
    