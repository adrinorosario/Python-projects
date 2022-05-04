# Lets now code a passoword generator. Simple yet effective.
import random

cap = 'QWERTYUIOPLKJHGFDSAMNBVCXZ'
low = cap.lower()
spc = "!@#$%^&*()-_?><.`~"
num = "1234567890"
joint = cap + low + spc + num


password = ""


def pgen(size):
    if size == 4:
        password = random.choice(
            cap) + random.choice(low) + random.choice(spc) + random.choice(num)
        return password
    elif size == 5:
        password = random.choice(
            cap) + random.choice(low) + random.choice(spc) + random.choice(num) + random.choice(joint)
        return password
    elif size > 5:
        print("We recommend a passoword of 8 characters")
        password = random.choice(
            cap) + random.choice(low) + random.choice(spc) + random.choice(num) + random.choice(joint) + str(random.randint(10, 99)) + random.choice(spc)
        return password


user_size = int(input("Enter the size of your desired password: "))
try:
    out = pgen(user_size)
    print(out)
except ValueError():
    print("Enter a number")
