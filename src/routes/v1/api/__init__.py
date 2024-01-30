from fastapi import APIRouter
from . import (
    club,
    competition,
    discipline,
    event,
    range,
    rcc_event
)

api_router = APIRouter()
api_router.include_router(club.router, prefix="/club")
api_router.include_router(competition.router, prefix="/competition")
api_router.include_router(discipline.router, prefix="/discipline")
api_router.include_router(event.router, prefix="/event")
api_router.include_router(range.router, prefix="/range")

#api_router.include_router(rcc_event.router, prefix="/rcc_event")