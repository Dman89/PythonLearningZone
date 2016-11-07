import random
import os
def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
# make a list of words
word_bank = [
    'dogpile',
    'automobile',
    'snowmobile',
    'america',
    'blueberry',
    'peace'
]
# pick a random word
# draw spaces
# take guess
# draw guessed letters and strikes
# print win or loss

while True:
    start = input("Press Enter/Return to Start, or Enter 'Q' to quit.")
    if start.lower() == "q":
        break
    secret_word = random.choice(word_bank)
    bad_guesses = []
    good_guesses = []
    while len(bad_guesses) < 7 and len(good_guesses) != len(set(secret_word)):
        print('\n\n')
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_ ', end='')
        print("""
Strikes {} / 7
""".format(len(bad_guesses)))
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print('You can only Guess a single letter.')
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You have already guessed that letter.")
            continue
        elif not guess.isalpha():
            print("You can only guess letters.")
            continue

        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print("You Win! The word is {} as you know".format(secret_word))
                break
        else:
            bad_guesses.append(guess)

    if len(set(good_guesses)) == len(set(secret_word)):
        print("You Win! The word is {} as you know".format(secret_word))
    else:
        print("You didn't guess it! My secret word was {}".format(secret_word))
