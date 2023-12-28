from fastapi import APIRouter, WebSocket


router = APIRouter()

@router.websocket("/{range_id}")
async def ws_range(websocket: WebSocket):
    return {"message": "Some logic to RCC events"}
    