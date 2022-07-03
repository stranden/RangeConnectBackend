from fastapi import FastAPI

from routes.v1.api import api_router as api_router_v1


app = FastAPI()

app.include_router(api_router_v1, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "RangeConnectBackend - Please see the API docs!"}

@app.get("/healthz", status_code=200)
async def healthz():
    return {"message": "Application ready"}

@app.get("/metrics", status_code=200)
async def metrics():
    return {"message": "Lots of metrics here"}

