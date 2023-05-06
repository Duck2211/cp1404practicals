CURRENT_TIME = 2022


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """classes function"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """return the string"""
        return f"{self.name} ({self.year}): ${self.cost:,.2f}"

    def get_age(self):
        """this function allows it to calculate to get the age"""
        age = CURRENT_TIME - self.year
        return age

    def is_vintage(self):
        """check if vintage or not"""
        age = self.get_age()
        if age > 50:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.year < other.year
