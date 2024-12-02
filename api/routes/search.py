
from fastapi import APIRouter, HTTPException

from models.stay import Stay

# quote
router = APIRouter()


@router.get("")
async def get_search(request_id: str):
    print('request_id', request_id)



@router.post("")
async def createSearch():
    stay = Stay()
