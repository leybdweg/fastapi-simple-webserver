
from models.available_stays import AvailableStaysService
from services.providers.first_provider import FirstProvider
from services.quote_provider import QuoteProvider

firstProvider = FirstProvider()
quoteProvider = QuoteProvider(firstProvider)
availableStays = AvailableStaysService(quoteProvider)


def get_available_stays() -> AvailableStaysService:
    return availableStays  # singleton to keep data in-memory
