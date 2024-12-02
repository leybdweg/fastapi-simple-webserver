from fastapi import APIRouter

from api.routes import search

api_router = APIRouter()
api_router.include_router(search.router, prefix="/search")