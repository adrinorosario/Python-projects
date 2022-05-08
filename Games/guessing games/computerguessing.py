# This is a guessing game where the computer tries to guess a number which itself generates.
# The user enters the limit for the guessing.
import random


def guessing(limit):
    """ The limit here is upto what number the computer can guess. The random number will also 
    be within that same limit. The computer will keep on running the while loop until the given condition
    below is met. Sort of a limited infinite loop """
    while True:
        random_number = random.randint(1, limit)
        guess = random.choice([x for x in range(limit+1)])
        if random_number == guess:
            print(f"done! \
                {random_number} -> {guess}")
            break
        else:
            print(f"Random number {random_number} -/- Computer choice {guess}")


guessing(1000)

# user_input = int(input("Enter a limit: "))
# guessing(user_input)
