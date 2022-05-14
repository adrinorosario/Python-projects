""" A ROCK PAPER SCISSORS GAME IN THE TERMINAL """
import random
import sys


def game():
    """ The user enter the first letter of each option. Once the result is calculated, it is displayed. The user
    is then given the option to continue the game or end it. """
    options = ['r', 'p', 's']
    while True:
        userin = str(
            input("\'r\':Rock, \'p\':Paper, \'s\':Scissors. Enter accordingly: "))
        comp = random.choice(options)
        if comp == 'r':
            if userin == 'p':
                x_1 = int(input('You win. Enter 1 for rematch and 0 to exit: '))
                if x_1:
                    game()
                else:
                    sys.exit()
            if userin == 's':
                x_2 = int(input('You lost. Enter 1 for rematch and 0 to exit: '))
                if x_2:
                    game()
                else:
                    sys.exit()

            if userin == 'r':
                print('Tie. Rematch.')
                game()
        if comp == 's':
            if userin == 'r':
                x_3 = int(
                    input('You win. Enter 1 for rematch and 0 to exit: '))
                if x_3:
                    game()
                else:
                    sys.exit()

            if userin == 'p':
                x_4 = int(input('You lost. Enter 1 for rematch and 0 to exit: '))
                if x_4:
                    game()
                else:
                    sys.exit()
            if userin == 's':
                print('Tie. Rematch.')
                game()
        if comp == 'p':
            if userin == 's':
                x_5 = int(input('You win. Enter 1 for rematch and 0 to exit: '))
                if x_5:
                    game()
                else:
                    sys.exit()
            if userin == 'r':
                x_6 = int(input('You lost. Enter 1 for rematch and 0 to exit: '))
                if x_6:
                    game()
                else:
                    sys.exit()
            if userin == 'p':
                print('Tie. Rematch.')
                game()


game()
