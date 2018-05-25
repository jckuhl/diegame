from roller import Roller
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
            pattern = re.compile(r'\d+d\d+')
            if pattern.match(dice_str) != None:
                dice = dice_str.split('d')
                dice_sides = abs(int(dice[1]))
                num_dice = abs(int(dice[0]))
                if(dice_sides < 100 and num_dice < 100):
                    roller = Roller(num_dice, dice_sides)
                    print('Rolling . . .\n')
                    sleep(1)
                    roller.roll()
                    print('Here are your rolls\n')
                    print(roller)
                else:
                    print('Your values are too big, try again')
            else:
                print('Try again.  The format is XdY')

if __name__ == '__main__':
    game()
