from fastapi import APIRouter
from routes.v1.endpoints import event, club, range, rcc_event

api_router = APIRouter()
api_router.include_router(event.router, prefix="/event")
api_router.include_router(club.router, prefix="/club")
api_router.include_router(range.router, prefix="/range")

api_router.include_router(rcc_event.router, prefix="/rcc_event")