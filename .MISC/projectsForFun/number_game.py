import random

secret_number = 0
guess = 0
high = 10
low = 0
trys = 0
guess_text = "Guess a number between {} and {}: ".format(low, high)


def print_welcome():
    print("""
Welcome to a number guessing game.
Type '-1' to end the game at anytime.
""")

# generate a random number
def generate_secret_number():
    global secret_number
    global trys
    trys = 0
    secret_number = random.randint(low, high)

# get a number guess from the player
def input_guess():
    global guess
    try:
        guess = int(input(guess_text))
    except ValueError:
        print("\nOh! Enter a Number Please.")
        guess = -2

#compare numbers
def compare_numbers():
    guess_number()
    #print hit or miss
    if guess == -1:
        print("Exiting...")
    elif guess == -2:
        print("")
    elif guess == secret_number:
        print("\n\nCorrect! My number was: {} and you got it in {} try(s)\n\n".format(secret_number, trys))
        generate_secret_number()
    elif guess > secret_number:
        print("\nGuess is too big\n")
    elif guess < secret_number:
        print("\nGuess is too small\n")

#print total trys
def guess_number():
    global trys
    if guess >= 0:
        trys += 1
        print("Guess #{}".format(trys))

#game loop
def main():
    print_welcome()
    generate_secret_number()
    while True:
        input_guess()
        if guess == -1:
            break
        compare_numbers()
main()
