from fastapi import FastAPI, Request
from typing import Any, Dict

from model import ModelOutput

app = FastAPI()

@app.get("/getXLSX")
async def root(request: Dict[Any, Any]):
    # request_body = await request.json()
    print(request)
    return "OK"