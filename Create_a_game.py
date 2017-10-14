import random

#variable containing a random number from the library
number = random.randint(1, 10)
tries = 1

#variable containing a string requesting user input
uname = input("Hello, what is your name?\n")

print("Hello", uname + ".",)

question = input("Would you like to play a game [Y/N]")

#conditional statement if user input is meets one of the two binary options
if question == "n":
    print("You are no fun!")

#conditional statement if user input is meets one of the two binary options
if question == "y":
    print("I'm thinking of a number between 1 and 10")

#variable containing a string asking for user input in the form of an integer
    guess = int(input("Can you figure it out?"))
    if guess > number:
        print("Incorrect. Guess lower...\n")
    if guess < number:
        print("Incorrect. Guess higher...\n")
#loop used to repeat the question if the number guessed is incorrect
    while guess != number:
        tries += 1
        guess = int(input("Try again:"))

#conditional statement if the user input is correct
    if guess == number:
        print("You are correct! Great Job!\n")
        print("This is the end of the game.  Thanks for playing!")
