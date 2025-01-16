from fastapi import APIRouter

from app.api.routes import search, metrics

api_router = APIRouter()
api_router.include_router(search.router, prefix="/search")
api_router.include_router(metrics.router, prefix="/metrics")