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
secret_number = []
guess_number = []
guesses = 0
bulls = 0
cows = 0


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

while game_runs:

    #creates a unique four-digit
    # secret number
    secret = random.randint(1, 9)
    if not secret in secret_number:
        secret_number.append(secret)
    else:
        continue
    if len(secret_number) == 4:
        begin = time.time()

        #game start
        while game_runs:

            guess = input("Enter a number: ")
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

            #checks if the guessed number contains duplicates
            if len(guess) == 4 and len(guess) == len(set(guess)):

                for number in guess:
                    guess_number.append(int(number))

                #check the presence of numbers, the common positions of numbers
                for num_secret, num_guess in zip(secret_number, guess_number):

                    if num_secret in guess_number and num_secret != num_guess:
                        cows += 1

                    if num_secret in guess_number and num_secret == num_guess:
                        bulls += 1

                    if bulls == 4:
                        print(secret_number)
                        print("Correct, you've guessed the right number")
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
                            print("Not so good...")
                            quit()

                #statement 'bulls, cows' in the correct uniform or plural form
                print(bulls, get_uniform_bull(bulls), ",", cows, get_uniform_cow(cows))
                print(separator)

                bulls = 0
                cows = 0
                guess_number.clear()

















































































