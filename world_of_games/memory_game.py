import random
import time

"""
The purpose of memory game is to display an amount of random numbers to the users for 0.7
seconds and then prompt them from the user for the numbers that he remember. If he was right
with all the numbers the user will win otherwise he will lose.
"""


def generate_sequence(difficulty):
    sequence = []
    for i in range(difficulty):
        sequence.append(random.randint(1, 101))
    return sequence


def print_sequence(sequence):
    print("Here is the sequence for you to remember:")
    sequence_text = str(sequence)
    print(sequence_text, end="", flush=True)
    time.sleep(0.7)
    print("\r" + " " * len(sequence_text), end="", flush=True)
    print("\r", end="", flush=True)


def get_list_from_user(difficulty):
    user_list = []
    for i in range(difficulty):
        user_list.append(int(input(f"Enter number {i+1}: ")))
    return user_list


def is_list_equal(sequence, user_list):
    return sequence == user_list


def play(difficulty):
    sequence = generate_sequence(difficulty)
    print_sequence(sequence)
    user_list = get_list_from_user(difficulty)
    if is_list_equal(sequence, user_list):
        print("You won!")
    else:
        print("You lost!")


if __name__ == "__main__":
    play(5)
