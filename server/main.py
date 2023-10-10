from fastapi import FastAPI
import asyncio
from Api.routesApi import routeApi
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

app = FastAPI()

origins = [
    config('FRONT_URL')
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(routeApi)
