from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

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
async def register(inadr:str, request: Request):
    global host_server

    host_server = inadr
    return {"address": request.client.host}

@app.get('/find')
async def find():
    return {"address": host_server}

@app.get('/')
async def root():
    return "hello"