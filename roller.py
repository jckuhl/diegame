from die import Dice


class Roller:

    def __init__(self, num_dice, dice_sides):
        self.num_dice = num_dice
        self.dice_sides = dice_sides
        self.dice = []
        self.values = []
        for _ in range(self.num_dice):
            self.dice.append(Dice(dice_sides))

    def roll(self):
        for die in self.dice:
            self.values.append(die.roll())
        return self.values

    def __str__(self):
        result = ''
        for die in self.dice:
            result += str(die.value) + ' '
        return result