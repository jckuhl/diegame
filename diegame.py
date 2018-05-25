from die import Dice
from roller import Roller
from time import sleep

def game():
    prompt = ''
    while prompt != 'n':
        prompt = input('Would you like to roll some dice? y/n  ')
        if(prompt.lower() == 'y'):
            dice_str = input('Enter a dice value in the format XdY\n'
                             ' where x is the number of die and\n'
                             ' y is the number of sides per die\n')
            # TODO: string validation
            roller = Roller(dice_str)
            print('Rolling . . .\n')
            sleep(1)
            roller.roll()
            print('Here are your rolls\n')
            print(str(roller))

if __name__ == '__main__':
    game()
