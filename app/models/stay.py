import uuid
from typing import Dict

from pydantic import BaseModel


class ProviderData(BaseModel):
    quote: any


class Stay(BaseModel):
    request_id: str | None = uuid.uuid4()
    ski_site: int
    from_date: str
    to_date: str
    group_size: int
    provider_datas: Dict[str, ProviderData] = {}
