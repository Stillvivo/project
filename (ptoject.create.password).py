# project create password

import string
import random as rand
from curses.ascii import isalpha, isdigit

while True:
    while True:
        length_input = input("please enter your length password(4-50): ")
        if not length_input.isdigit():
            print("invalid length.please enter your length password.")
            continue
        length = int(length_input)
        if length < 4 or length > 50:
            print("please enter a number between 50 and 40.")
            continue
        else:
            break

    char = string.ascii_letters + string.digits + string.punctuation
    password = "".join(rand.choice(char) for i in range(length))

    print(f"your password is: ({password})")

    while True:
        answer = input("do you want to continue? (y/n)").lower()
        if answer == "y":
            break
        elif answer == "n":
            print("GoodBye")
            exit()
        else:
            print(f"{answer} is not a valid answer.Please try again.(y/n)")
