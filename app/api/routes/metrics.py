from fastapi import APIRouter

router = APIRouter()

@router.get("")
async def get_status(request_id: str):
    return { # only mock data cuz my machine doesnt have enough resources to run prometheus
        "REQUEST_COUNT": 10,
        "CPU_USAGE": 0.7,
        "MEMORY_USAGE": 48000,
        "request_id": request_id
    }