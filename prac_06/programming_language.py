class ProgrammingLanguage:
    """Represents a programming language"""

    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming Language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        """Check if language is dynamically typed or not"""
        return self.typing == "Dynamic"
