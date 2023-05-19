class Band:
    def __init__(self, name=""):
        """the function will initialise the name,members."""
        self.name = name
        self.members = []
        self.members_dictionary = {}

    def __str__(self):
        """returning string"""
        return f"{self.name} ({str(self.members).lstrip('[').rstrip(']')})"

    def add(self, musician):

        self.members_dictionary[musician.name] = musician.instruments
        self.members.append(f"{musician.name} ({musician.instruments})")

    def play(self):
        for member in self.members_dictionary:
            if not self.members_dictionary[member]:
                print(f"{member} needs an instrument!")
            else:
                print(f"{member} is playing: {self.members_dictionary[member][0]}")
