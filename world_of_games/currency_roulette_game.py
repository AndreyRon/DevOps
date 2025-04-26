import random
import requests

"""
This game will use the free currency api to get the current exchange rate from USD to ILS, will
generate a new random number between 1-100 a will ask the user what he thinks is the value of
the generated number from USD to ILS, depending on the user's difficulty his answer will be
correct if the guessed value is between the interval surrounding the correct answer
currency_api_url = "https://api.exchangerate-api.com/v4/latest/USD"
"""


def get_current_exchange_rate():
    # Retrieve the current USD to ILS exchange rate from the external API
    currency_api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(currency_api_url)
    data = response.json()
    exchange_rate = data["rates"]["ILS"]
    return exchange_rate


def get_money_interval(difficulty, total_money):
    # Calculate the acceptable range for the user's guess based on difficulty
    low_interval = total_money - (5 - difficulty)
    high_interval = total_money + (5 - difficulty)
    return low_interval, high_interval


def get_random_number(exchange_rate):
    # Generate a random USD amount and calculate its value in ILS
    random_number = random.randint(1, 100)
    total_money = random_number * exchange_rate
    return total_money, random_number


def get_guess_from_user(random_number):
    # Prompt the user to guess the ILS value of the random USD amount
    guess = int(
        input(f"Enter your guess for the value of {random_number} USD in ILS: ")
    )
    return guess


def play(difficulty):
    # Main game function that coordinates the game flow and determines the result
    exchange_rate = get_current_exchange_rate()
    total_money, random_number = get_random_number(exchange_rate)
    low_interval, high_interval = get_money_interval(difficulty, total_money)
    guess = get_guess_from_user(random_number)
    if guess <= high_interval and guess >= low_interval:
        print("You won!")
        return True
    else:
        print("You lost!")
        return False


if __name__ == "__main__":
    play(difficulty)
