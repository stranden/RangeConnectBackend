from fastapi import FastAPI

from routes.v1.api import api_router as api_router_v1


app = FastAPI()

app.include_router(api_router_v1, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Hello RangeConnectBackend - Please see the API docs!"}
    