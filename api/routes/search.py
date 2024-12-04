from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from di import availableStays
from models.stay import Stay

# quote
router = APIRouter()


class CreateSearchResponse(BaseModel):
    id: str


@router.get("")
async def get_search(request_id: str) -> Stay | None:
    foundStay = availableStays.get_stay_by_request_id(request_id)
    print('get_search', request_id, foundStay)
    return foundStay


@router.post("")
async def createSearch(body: Stay) -> str:
    # stay = available_stays.set_stay(body)
    return 'stay.request_id'
