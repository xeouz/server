from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    ''' Run at startup
        Initialise the Client and add it to app.state
    '''
    app.state.data = {}
    yield
    ''' Run on shutdown
        Close the connection
        Clear variables and release the resources
    '''
    app.state.data = {}

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.post('/register')
async def register(inadr:str, request: Request):
    request.app.state.data['host'] = inadr
    return {"address": request.app.state.data['host']}

@app.get('/find')
async def find(request: Request):
    return {"address": request.app.state.data['host']}

@app.get('/')
async def root():
    return "hello"