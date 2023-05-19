import random
from prac_06.car import Car


class Unreliable_car(Car):
    def __init__(self, name, fuel, reliability=float):
        """initializing car,fuel and reliability"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car but also calculate the distance also."""
        if random.uniform(0,100) < float(self.reliability):
            return super().drive(distance)
        else:
            return 0
