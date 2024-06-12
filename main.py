from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

host_server = ""

@app.post('/register')
def register(request: Request):
    print(request)
    return {}

@app.get('/test')
def test():
    return "hello"

uvicorn.run(app, port=6900)