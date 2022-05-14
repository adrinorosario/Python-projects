""" A TERMINAL GUI GAME OF TIC TAC TOE """
import random


PUZZLE_NUMBERING_PATTERN = """
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9 """

MOCK_2 = """
|  |  |  |
|  |  |  |
|  |  |  | """

print(PUZZLE_NUMBERING_PATTERN)
print("Take a look at the board. Enter the number on the board. \
For example, if you are X and enter 5, the place of 5 will be yours, that is X.")

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
cl = [x for x in range(1, 10)]


def game():
    """ game module """
    counter = 0
    counter2 = 0
    while counter < 10 and counter2 < 10:
        print("You can enter from the following choices: ",)
        for items in cl:
            print(items, end=" ")
        ch = int(input("Enter your move: "))
        if board[ch-1] != 0:
            if counter == 0:
                print("The place is already filled, try again!")
                game()
            if counter > 0:
                print("The place is already filled, try again!")
                counter -= 1
                game()
        if board[ch-1] == 0:
            board[ch-1] = 'X'
            counter += 1
            cl.remove(ch)

        comp = random.choice(cl)
        if board[comp-1] != 0:
            if counter2 == 0:
                print("The place is already filled, try again!")
                game()
            if counter2 > 0:
                print("The place is already filled, try again!")
                counter2 -= 1
                game()
        if board[comp-1] == 0:
            board[comp-1] = 'O'
            counter2 += 1
            cl.remove(comp)

        for i in range(len(board)):
            if i == 2 or i == 5:
                if board[i] == 0:
                    print("|" + " ", end="| \n")
                else:
                    print("|" + board[i], end="| \n")
            else:
                if board[i] == 0:
                    print("|" + " ", end="|")
                else:
                    print("|" + board[i], end="|")
        print("\n ____________________________________________________")

        if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X') or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X'):
            print("X wins the game")
            break
        if (board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O') or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O'):
            print("Computer wins the game")
            break


game()
