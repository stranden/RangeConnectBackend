from fastapi import APIRouter
from routes.v1.endpoints import event, club

api_router = APIRouter()
api_router.include_router(event.router, prefix="/event")
api_router.include_router(club.router, prefix="/club")