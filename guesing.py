# lets creat a guessing game in python
# the range of guessing is from 1 to 10
import random

number = random.randrange(1,10)
print(number)

def guess():
    i = 0
    while i < 3 :
        guess = input("guess a number in the range 1 to 10: ")
        if int(guess) > number:
            print("too high")
        elif int(guess) < number:
            print("too high")
        else:
            print(f" correct, the number is {number}")
            return

        i += 1

    print("sorry your 3 tries are over")

guess()
