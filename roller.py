from die import Dice

class Roller:

    def __init__(self, die_str):
        dice = die_str.split('d')
        self.size = int(dice[0])
        self.dice = []
        self.values = []
        for _ in range(int(dice[1])):
            self.dice.append(Dice(self.size))

    def roll(self):
        for die in self.dice:
            self.values.append(die.roll())
        return self.values

    def __str__(self):
        result = ''
        for die in self.dice:
            result += str(die.value) + ' '
        return result