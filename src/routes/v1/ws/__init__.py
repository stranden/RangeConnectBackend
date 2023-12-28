from fastapi import APIRouter
from . import (
    range
)

api_router = APIRouter()
api_router.include_router(range.router, prefix="/range")