import uuid
from http import HTTPStatus
from typing import List, Optional

from fastapi import APIRouter, Depends, Response
from fastapi.exceptions import HTTPException


router = APIRouter()

@router.get("/")
async def event():
    return {"message": "GET All clubs"}