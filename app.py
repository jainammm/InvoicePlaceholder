from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/getXLSX")
async def root(request: Request):
    request_body = await request.json()
    print(request_body['model_output'][0]['bounding_box'])
    return "OK"