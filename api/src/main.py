from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def read_root(request: Request):
    print(f"Request = {request.client.host}")
    return {"Hello there visitor from": request.client.host}
