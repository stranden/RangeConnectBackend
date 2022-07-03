from fastapi import FastAPI

from routes.v1.api import api_router as api_router_v1


description = """
RangeConnectBackend API helps you do awesome stuff.

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="RangeConnectBackend",
    description=description,
    version="0.0.1",
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    }
)

app.include_router(api_router_v1, prefix="/api/v1")


@app.get("/", include_in_schema=False)
async def root():
    return {"message": "RangeConnectBackend - Please see the API docs!"}

@app.get("/healthz", status_code=200, tags=["Deployment"])
async def healthz():
    return {"message": "Application ready"}

@app.get("/metrics", status_code=200, tags=["Deployment"])
async def metrics():
    return {"message": "Lots of metrics here"}

