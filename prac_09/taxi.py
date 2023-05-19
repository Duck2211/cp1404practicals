from prac_06.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23

    def __init__(self, name, fuel):
        """initialising a Taxi"""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """the function will return the string """
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f})/km"

    def collect_fare(self):
        """the function will do the get fare from the car driving"""
        return round(self.price_per_km * self.current_fare_distance, 1)

    def start_fare(self):
        """this function will start the fare"""
        self.current_fare_distance = 0

    def drive(self, distance):
        """this function calculate the distance driven and fare """
        distance_drove = super().drive(distance)
        self.current_fare_distance += distance_drove
        return distance_drove
