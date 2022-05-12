import wikipedia
import sys
from colorama import Fore

storage2 = dict()
storage1 = dict()


def recur_search(lst):
    ch = int(input(
        "Enter the number of the thing from above list you wish to search from above list, 0 to exit: "))
    if ch:
        res = wikipedia.search(lst[ch-1])
        for items in res:
            print(items)
    else:
        sys.exit()


def search():
    choice = int(input("Enter 1 to search everything related to your search, 2 to get the summary of your search, 3 to suggest a suitable answer to your searched input: "))
    userin = input("Enter what you wish to search: ")
    try:

        # first type of search
        if choice == 1:
            if userin in storage2.keys():
                out1 = storage2.get(userin)
                for i, items in enumerate(out1):
                    print(f'{i}- {items}')
                recur_search(out1)
            else:
                ls = wikipedia.search(userin)
                storage2[userin] = ls
                for i, items in enumerate(ls):
                    print(f'{i+1}- {items}')
                recur_search(ls)

        # Second type of search
        if choice == 2:
            if userin not in storage1.keys():
                resl = wikipedia.summary(userin, sentences=3)
                print(resl)
                storage1['userin'] = resl
            if userin in storage1.keys():
                out = storage1.get(userin)
                print(out)

    except TypeError():
        print("Enter a suitable query")


search()
