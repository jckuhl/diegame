from die import Dice

class DieTooLargeError(Exception):

    def __init__(self, message):
        self.message = message

    @staticmethod
    def getMessage(self):
        return self.message


class Roller:

    def __init__(self, die_str):
        dice = die_str.split('d')
        self.num_die = abs(int(dice[0]))
        self.size = abs(int(dice[1]))
        self.dice = []
        self.values = []
        if self.size > 100 or self.num_die > 100:
            raise DieTooLargeError(f'{self.size} or {self.num_die} is too large.\n'
                                   f'Please limit yourself to 100 or fewer')
        for _ in range(self.num_die):
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