from datetime import datetime as dt
from fastapi import FastAPI, Request
import logging


app = FastAPI()

@app.get("/visitors")
async def read_root(request: Request):
    logging.info(f'Incoming visitor from {request.client.host}')
    return {"ip": request.client.host,"date": dt.now()}
