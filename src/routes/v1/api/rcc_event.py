import uuid
from http import HTTPStatus
from typing import List, Optional

from fastapi import APIRouter, Depends, Response
from fastapi.exceptions import HTTPException


router = APIRouter()

@router.get("/", tags=["RangeConnectClient"])
async def rcc_event():
    return {"message": "Some logic to RCC events"}
    