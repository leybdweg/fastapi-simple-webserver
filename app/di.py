
from app.models.available_stays import AvailableStaysService
from app.services.providers.first_provider import FirstProvider
from app.services.quote_provider import QuoteProvider

firstProvider = FirstProvider()
quoteProvider = QuoteProvider(firstProvider)
availableStays = AvailableStaysService(quoteProvider)
