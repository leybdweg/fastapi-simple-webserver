import asyncio
from typing import List

from app.db import reserverDb
from app.models.stay import Stay
from app.services.quote_provider import QuoteProvider


class AvailableStaysService:
    available_stays_offers: List[Stay] = []
    keep_quote_loop_alive = True
    quote_loop_interval = 10
    providers: List[str] = ['first', 'second']

    def __init__(self, quote_provider: QuoteProvider):
        self.quoteProvider = quote_provider

    async def set_stay(self, stay: Stay) -> Stay:
        self.available_stays_offers.append(stay)
        await reserverDb.stays.insert_one(stay.model_dump())

        return stay

    async def get_stay_by_request_id(self, request_id: str) -> Stay | None:
        offer_found = next((stay for stay in self.available_stays_offers if stay.request_id == request_id),
                           None)
        if offer_found:
            return offer_found

        from_db = await reserverDb.stays.find_one({'request_id': request_id})
        return from_db

    async def init(self):
        print('starting async init')
        while self.keep_quote_loop_alive:
            await asyncio.sleep(self.quote_loop_interval)
            try:
                await self.update_quotes()
            except Exception as e:
                print('keep_quote_loop_alive error', e)

    async def update_quotes(self):
        for offer in self.available_stays_offers:
            for provider in self.providers:  # TODO: gather all Futures and do single await
                if not offer.provider_datas.get(provider, False):
                    quote = await self.quoteProvider.fetch_quote(provider, offer)
                    offer.provider_datas[provider] = quote
            # TODO: this can be moved outside of memory already, maybe TTL cache?
            await reserverDb.stays.update_one({'request_id': offer.request_id},
                                              {'$set':
                                                   {"provider_datas": offer.provider_datas}})
