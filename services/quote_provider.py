from typing import Any

from models.stay import Stay
from services.providers.first_provider import FirstProvider


class QuoteProvider:

    def __init__(self, first_provider: FirstProvider):
        self.first_provider = first_provider

    def fetch_quote(self, provider: str, stay: Stay) -> Any:
        match provider:
            case 'first_provider':
                return self.first_provider.fetch_quote(stay)
            case _:
                raise ValueError(f'Unknown provider: {provider}')

