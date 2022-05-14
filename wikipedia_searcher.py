import wikipedia

storage2 = dict()
storage1 = dict()
storage3 = dict()


def search():
    """ This is the method that implements the search. Takes options and searches using three different types of ways
    Comments listed below"""
    choice = int(input("Enter 1 to search everything related to your search, 2 to get the summary of your search, 3 to suggest a suitable answer to your searched input: "))
    userin = input("Enter what you wish to search: ")
    try:

        # first type of search- prints everything related to your search query
        if choice == 1:
            if userin in storage2.keys():
                out1 = storage2.get(userin)
                for i, items in enumerate(out1):
                    print(f'{i}- {items}')
                print("\n")
                ch = int(input(
                    "Enter the number of the thing from above list you wish to search from above list: "))
                res1 = wikipedia.search(out1[ch-1])
                for items1 in res1:
                    print(items1)
                search()

            elif userin not in storage2.keys():
                ls = wikipedia.search(userin)
                storage2[userin] = ls
                for i, items in enumerate(ls):
                    print(f'{i+1}- {items}')
                print("\n")
                chs = int(input(
                    "Enter the number of the thing from above list you wish to search from above list: "))
                re2 = wikipedia.search(ls[chs-1])
                for items1 in re2:
                    print(items1)
                search()

        # Second type of search-  gives you a answer to your search
        if choice == 2:
            try:
                if userin not in storage1.keys():
                    resl = wikipedia.summary(userin, sentences=3)
                    print(resl + "\n")
                    storage1['userin'] = resl
                    search()
                elif userin in storage1.keys():
                    out = storage1.get(userin)
                    print(out + "\n")
                    search()
            except wikipedia.exceptions.DisambiguationError as op:
                print("There are a lot of things that relate to your search query. Select what you wanted to search from below and search again: ")
                print(op.options + "\n")
                search()
            except wikipedia.exceptions.PageError:
                print(
                    f"There is nothing availabe related to {userin}. Try searching something else: " + "\n")
                search()

        # third type of search-  suggests something related to your search
        if choice == 3:
            if userin not in storage3.keys():
                res = wikipedia.suggest(userin)
                print(res + "\n")
                storage3[userin] = res
                search()
            elif userin in storage3.keys():
                print(storage3.get(userin) + "\n")
                search()

    except TypeError():
        print("Enter a suitable query")


search()
