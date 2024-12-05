from fastapi import APIRouter

from app.api.routes import search

api_router = APIRouter()
api_router.include_router(search.router, prefix="/search")