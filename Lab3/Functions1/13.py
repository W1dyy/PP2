import random

print("Hello! What is your name?")
y = input()

print("Well, ", y, "I am thinking of a number between 1 and 20.")

attempts = 0
number = random.randint(1, 20)

while True:
    print("Take a Guess.")
    x = int(input())
    attempts += 1

    if x < number:
        print("Your guess is too low.")
    elif x > number:
        print("Your guess is too high.")
    else:
        print("Good job, ",y, " You guessed my number in ",x, " guesses!")
        break


