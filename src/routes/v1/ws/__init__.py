from fastapi import APIRouter
from . import (
    range
)

ws_router = APIRouter()
ws_router.include_router(range.router, prefix="/range")