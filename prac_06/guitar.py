class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Determine the age of the guitar"""
        return 2020 - self.year

    def is_vintage(self):
        """Check if guitar is classified as vintage"""
        return self.get_age() >= 50
