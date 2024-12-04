import asyncio
import uuid
from typing import List

from models.stay import Stay
from services.quote_provider import QuoteProvider


class AvailableStaysService:
    available_stays_offers: List[Stay] = []
    keep_quote_loop_alive = True
    quote_loop_interval = 5
    providers: List[str] = ['first', 'second']

    def __init__(self, quote_provider: QuoteProvider):
        self.quoteProvider = quote_provider

    def set_stay(self, stay: Stay) -> Stay:
        stay.request_id = uuid.uuid4()
        self.available_stays_offers.append(stay)

        return stay

    def get_stay_by_request_id(self, request_id: str) -> Stay | None:
        offer_found = next((offer for offer in self.available_stays_offers if offer['request_id'] == request_id),
                           None)

        return offer_found

    async def init(self):
        while self.keep_quote_loop_alive:
            print('starting async init')
            await self.update_quotes()

    async def update_quotes(self):
        print('update_quotes000', self.available_stays_offers)
        for offer in self.available_stays_offers:
            for provider in self.providers:
                if offer.provider_datas[provider] is None:
                    quote = await self.quoteProvider.fetch_quote(offer)
                    offer.provider_datas[provider] = quote
        await asyncio.sleep(self.quote_loop_interval)

