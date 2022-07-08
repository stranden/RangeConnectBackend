from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from routes.v1.api import api_router as api_router_v1
from settings import Settings
from util import logging


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
    },
    docs_url="/docs",
    redoc_url=None
)

app.include_router(api_router_v1, prefix="/api/v1")

@app.get("/healthz", status_code=200, tags=["Deployment"])
async def healthz():
    return {"message": "Application ready"}

@app.get("/metrics", status_code=200, tags=["Deployment"])
async def metrics():
    return {"message": "Lots of metrics here"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
    data = await request.json()
    logging.error(f"{request}: {data}")
    logging.error(f"{request}: {exc_str}")
    content = {'status_code': 10422, 'message': exc_str, 'data': None}

    return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)