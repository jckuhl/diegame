from random import randint

class Dice:

    def __init__(self, sides):
        self.sides = sides
        self.value = 0

    def roll(self):
        self.value = randint(1, self.sides)
        return self.value

    def __str__(self):
        return f'{self.value}d{self.sides}'

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __rsub__(self, other):
        return self.value - other

    def __eq__(self, other):
        return self.value == other

    def __gt__(self, other):
        return self.value > other

    def __ge__ (self, other):
        return self.value > other or self.value == other

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.valye < other or self.value == other

