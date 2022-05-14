""" In this game, the computer generates a random number and the user tries to guess the number. """
import random as r


def guess():
    """ This is the game module. On invoking the method, it will prompt the user to enter a number between two
    limits. If the user gets the guess wrong or right, the suitable message will be displayed and an option will be
    provided if the user wants to play a new game or exit. the user then has to operate or input initials accordingly
    """
    limit = r.randint(1, 100)
    randomnum = r.choice([x for x in range(1, limit+1)])
    print(f'You now have to guess a number between 1 and {limit}')
    userin = int(input("Enter your guess: "))
    while userin:
        if userin == randomnum:
            print('Your have won!')
            choice = str(
                input("Enter \'r\' if you want to play again or \'e\' to exit: "))
            if choice == 'r':
                guess()
            elif choice == 'e':
                break
        elif userin != randomnum:
            choice = str(input(f"Sorry you have lost. The number was {randomnum} and your guess was {userin}. \
                 Enter \'r\' if you want a rematch or \'e\' to exit: "))
            if choice == 'r':
                guess()
            elif choice == 'e':
                break


guess()
