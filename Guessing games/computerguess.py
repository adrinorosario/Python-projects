# In this game, you enter a number within a limit and the computer tries to guess the number.
# Wrong guess starts a new game and a correct guess exits the game or ends it.
import random


def game():
    """ This is the game module"""
    limit = random.randint(1, 1000)
    userin = int(input(f"Enter a number between 1 and {limit}"))
    computerin = random.choice([x for x in range(1, limit)])
    while True:
        if computerin == userin:
            print(f'{userin} -> {computerin}. Computer guessed right')
            break
        else:
            print(f'{computerin} is not {userin}')
            game()


game()
