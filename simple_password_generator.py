""" Lets now code a passoword generator. Simple yet effective. """
import random

CAP = 'QWERTYUIOPLKJHGFDSAMNBVCXZ'
LOW = CAP.lower()
SPC = "!@#$%^&*()-_?><.`~"
NUM = "1234567890"
JOINT = CAP + LOW + SPC + NUM


def pgen(size):
    password = ""
    if size == 4:
        password = random.choice(
            CAP) + random.choice(LOW) + random.choice(SPC) + random.choice(NUM)
        return password
    elif size == 5:
        password = random.choice(
            CAP) + random.choice(LOW) + random.choice(SPC) + random.choice(NUM) + random.choice(JOINT)
        return password
    elif size > 5:
        print("We recommend a passoword of 8 characters")
        password = random.choice(
            CAP) + random.choice(LOW) + random.choice(SPC) + random.choice(NUM) + random.choice(JOINT) + str(random.randint(10, 99)) + random.choice(SPC)
        return password


user_size = int(input("Enter the size of your desired password: "))
try:
    out = pgen(user_size)
    print(out)
except ValueError():
    print("Enter a number")
