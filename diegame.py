from die import Dice
from roller import Roller, DieTooLargeError
from time import sleep
import re


def game():
    prompt = ''
    while prompt != 'n':
        prompt = input('Would you like to roll some dice? y/n  ')
        if(prompt.lower() == 'y'):
            dice_str = input('Enter a dice value in the format XdY\n'
                             ' where x is the number of die and\n'
                             ' y is the number of sides per die\n')
            # TODO: string validation
            pattern = re.compile(r'\d+d\d+')
            if pattern.match(dice_str) != None:
                try:
                    roller = Roller(dice_str)
                    print('Rolling . . .\n')
                    sleep(1)
                    roller.roll()
                    print('Here are your rolls\n')
                    print(roller)
                except DieTooLargeError:
                    print(DieTooLargeError.getMessage());
            else:
                print('Try again.  The format is XdY')

if __name__ == '__main__':
    game()
