import random

"""
The purpose of guess game is to start a new game, cast a random number between 1 to a
variable called difficulty. The game will get a number input from the
user and compare it to the secret number.
"""


def generate_number(difficulty):
    # Generate a random number between 1 and the difficulty level
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    # Get the user's guess input for a number between 1 and difficulty
    guess = int(input(f"Guess a number between 1 and {difficulty}: "))
    return guess


def compare_results(secret_number, guess):
    # Compare the user's guess with the secret number and return True if they match
    return secret_number == guess


def play(difficulty):
    # Main game function - generates number, gets user's guess, and determines the result
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    result = compare_results(secret_number, guess)
    if result:
        print("You won!")
    else:
        print("You lost!")


if __name__ == "__main__":
    play(difficulty)
