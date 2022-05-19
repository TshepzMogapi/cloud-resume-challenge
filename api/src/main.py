
from fastapi import FastAPI, Request
import logging


app = FastAPI()

@app.get("/visitors")
async def read_root(request: Request):
    logging.info(f'Incoming visitor from {request.client.host}')
    return {"Hello there visitor from": request.client.host}
