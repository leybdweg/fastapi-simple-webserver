from typing import Dict

from pydantic import BaseModel


class ProviderData(BaseModel):
    quote: any


class Stay(BaseModel):
    ski_site: int
    from_date: str
    to_date: str
    group_size: int
    provider_datas: Dict[str, ProviderData] = {}
