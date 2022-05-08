""" Fizz Buzz is a very simple programming task, asked in software developer job interviews. 
A typical round of Fizz Buzz can be: Write a program that prints the numbers from 1 to 100 and 
for multiples of '3' print “Fizz” instead of the number and for the multiples of '5' print “Buzz”. """

for i in range(1, 101):
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")
    if i % 3 != 0 and i % 5 != 0:
        print(i)
