from random import random, randint

import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_level(level):
    if level == "easy":
        return EASY_LEVEL_TURNS

    return HARD_LEVEL_TURNS


def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    turns = set_level(level)
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > answer:
            print("Too High")
        elif guess < answer:
            print("Too Low.")
        else:
            print(f"You got it! The answer was {answer}")

        turns = turns - 1

        if turns == 0:
            print("You've run out of guesses, you lose.")
            again = input("Play Again ? y/n : ").lower()
            if again == "n":
                break
            print("\n"*20)
            play_game()

        print("Guess again")


play_game()