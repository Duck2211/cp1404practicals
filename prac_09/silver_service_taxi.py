from taxi import Taxi


class SilverServiceTaxi(Taxi):
    price_per_km = Taxi.price_per_km
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = fanciness * self.price_per_km

    def __str__(self):
        """return the string"""
        return f"{super().__str__()} plus flagfall of {self.flagfall}"

    def collect_fare(self):
        """collecting fare in this functiom"""
        return super().collect_fare() + self.flagfall
