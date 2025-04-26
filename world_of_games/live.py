import memory_game
import guess_game
import currency_roulette_game


def welcome_message(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).")
    print("Here you can find many cool games to play.")


def load_game():
    try:
        print("Please choose a game to play:")
        print(
            "1. Memory Game - a sequence of numbers will appear for 1 second and then disappear."
        )
        print("2. Guess Game - guess a number and see if you chose like the computer.")
        print(
            "3. Currency Roulette - try and guess the value of a random amount of USD in ILS."
        )
        try:
            game_choice = int(
                input("Enter the number of the game you want to play from 1 to 3:")
            )
        except ValueError:
            print("Invalid input!!!. Please enter a valid number from 1 to 3.")
            return load_game()
        difficulty = int(input("Please choose game difficulty from 1 to 5:"))
        if game_choice == 1:
            result = memory_game.play(difficulty)
        elif game_choice == "2":
            result = guess_game.play(difficulty)
        elif game_choice == "3":
            result = currency_roulette_game.play(difficulty)
            return result
    except ValueError:
        print("Invalid input. Please enter a valid number from 1 to 3.")
        return load_game(5)
