""" Binary search implementation in Python """
import random

limit = random.randint(1, 10000)
lst = [x for x in range(1, limit+1)]  # computer generated list

choice = random.choice(lst)  # computer chooses the number to search
lb, ub, mid = 0, len(lst) - 1, 0

while lb <= ub:
    POS = 0
    mid = (lb+ub)/2
    mid2 = int(mid)
    # if the number is greater than middle value, the search will focus on the right half
    if choice > lst[mid2]:
        lb = mid2 + 1
    # if the number is smaller than middle value, the search will focus on the left half
    if choice < lst[mid2]:
        ub = mid2 - 1
    if choice == lst[mid2]:
        POS = mid2  # extracting the index
        break

print(f"Index of element {choice}: {POS}")

# above search works on an ascendingly sorted list\array. For a descending array, its the opposite:
"""
while lb <= ub:
    pos = 0
    mid = (lb+ub)/2
    mid2 = int(mid)
    if choice > lst[mid2]:
        ub = mid2 - 1
    if choice < lst[mid2]:
        lb = mid2 + 1
    if choice == lst[mid2]:
        pos = mid2
        break
"""
