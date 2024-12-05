from app.models.stay import Stay


class AvailableStaysService:
    available_stays_offers = []

    def set_stay(self, stay: Stay) -> Stay:
        self.available_stays_offers.append(stay)

        return stay