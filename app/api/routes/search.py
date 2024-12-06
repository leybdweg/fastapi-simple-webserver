from fastapi import APIRouter
from pydantic import BaseModel

from app.di import availableStays
from app.models.stay import Stay

# quote
router = APIRouter()


class CreateSearchResponse(BaseModel):
    id: str


@router.get("")
async def get_search(request_id: str) -> Stay | None:
    foundStay = await availableStays.get_stay_by_request_id(request_id)
    return foundStay


@router.post("")
async def createSearch(body: Stay) -> Stay:
    stay = await availableStays.set_stay(body)
    return stay
