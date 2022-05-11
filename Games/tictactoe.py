import random

mock = """
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9 """

board = f"""
{a} | {b} | {c}
{d} | {e} | {f}
{g} | {h} | {i}"""

print("Take a look at the board. Enter the number on the board. \
For example, if you are X and enter 5, the place of 5 will be yours, that is X.")


def game():
    x = int(input("Make your move: "))
