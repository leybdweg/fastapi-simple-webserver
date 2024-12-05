from typing import Any

from app.models.stay import Stay
from app.services.providers.first_provider import FirstProvider


class QuoteProvider:

    def __init__(self, first_provider: FirstProvider):
        self.first_provider = first_provider

    async def fetch_quote(self, provider: str, stay: Stay) -> Any:
        match provider:
            case 'first':
                return await self.first_provider.fetch_quote(stay)
            case _:  # in real life, this should throw error
                print(f'Unknown provider: {provider}')
