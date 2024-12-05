import asyncio
import uuid
from typing import List

from models.stay import Stay
from services.quote_provider import QuoteProvider


class AvailableStaysService:
    available_stays_offers: List[Stay] = []
    keep_quote_loop_alive = True
    quote_loop_interval = 10
    providers: List[str] = ['first', 'second']

    def __init__(self, quote_provider: QuoteProvider):
        self.quoteProvider = quote_provider

    def set_stay(self, stay: Stay) -> Stay:
        stay.request_id = uuid.uuid4()
        self.available_stays_offers.append(stay)

        return stay

    def get_stay_by_request_id(self, request_id: str) -> Stay | None:
        offer_found = next((stay for stay in self.available_stays_offers if stay.request_id == request_id),
                           None)

        return offer_found

    async def init(self):
        while self.keep_quote_loop_alive:
            print('starting async init')
            await asyncio.sleep(self.quote_loop_interval)
            try:
                await self.update_quotes()
            except Exception as e:
                print('keep_quote_loop_alive error', e)

    async def update_quotes(self):
        for offer in self.available_stays_offers:
            for provider in self.providers:
                if not offer.provider_datas.get(provider, False):
                    quote = await self.quoteProvider.fetch_quote(provider, offer)
                    offer.provider_datas[provider] = quote
