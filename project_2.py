"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: David Rakovsky
email: david.rakovsky@centrum.cz
discord: David R.#9097
"""
import random

import time

separator = "-" * 48
game_runs = True
guess_number = []
guesses = 0
bulls = 0
cows = 0
secret = random.randint(1000, 9999)

def generate_four_digit_number(num):
    while True:
        if len(str(num)) == len(set(str(num))):
            return num
        else:
            num = random.randint(1000, 9999)
            continue

def get_uniform_bull(num):
    #returns a uniform word shape
    if bulls == 0 or bulls > 1:
        return "bulls"
    else:
        return "bull"

def get_uniform_cow(num):
    # returns a uniform word shape
    if cows == 0 or cows > 1:
        return "cows"
    else:
        return "cow"

print("Hi there!")

print(separator)
print(""" I've generated a random 4 digit number for you.
Let"s play a bull and cow game.""")
print(separator)

secret_number = generate_four_digit_number(secret)

#game start
begin = time.time()
while game_runs:

    guess_number.clear()
    guess = input("Enter a number: ")
    guess_number = [number for number in guess]
    print(separator)
    guesses += 1

    #checking user inputs
    if not guess.isnumeric():
        print("Your entry must contain numbers only!")
        continue

    if str(guess).startswith("0"):
        print("Your entry must not start with a zero!")
        continue

    if len(guess) != 4:
        print("Your entry must be four numbers only!")
        continue

    if len(guess) != len(set(guess)):
        print("Your entry must not contain duplicates!")
        continue

    #check the presence of numbers, the common positions of numbers
    for num_secret, num_guess in zip(str(secret_number), guess_number):

        if num_secret in guess_number and num_secret != num_guess:
            cows += 1

        if num_secret in guess_number and num_secret == num_guess:
            bulls += 1

        if bulls == 4:
            print(secret)
            print(f"in {guesses} guesses!")
            print()
            end = time.time()
            game_time = end - begin
            print(f"Game time {int(game_time)} seconds")
            print(separator)

            if 0 < guesses <= 4:
                print("That's amazing!")
                quit()

            if 4 < guesses <= 7:
                print("That's average.")
                quit()

            if 7 < guesses:
                int("Not so good...")
                quit()

    #statement 'bulls, cows' in the correct uniform or plural form
    print(bulls, get_uniform_bull(bulls), ",", cows, get_uniform_cow(cows))
    print(separator)

    bulls = 0
    cows = 0
