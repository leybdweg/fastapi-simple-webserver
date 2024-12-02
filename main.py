from fastapi import FastAPI
from api.routes.main import api_router

app = FastAPI(
    title="we rock"
)

app.include_router(api_router)