"""
Week 1 Mini Project: Number Guessing Game + Simple Calculator
A single-file CLI application combining two beginner Python programs.
"""

import random

# NUMBER GUESSING GAME

def get_difficulty():
    """Ask the player to choose a difficulty level and return (low, high, max_guesses)."""
    print("\nChoose a difficulty:")
    print("  1. Easy    (1-50,  10 guesses)")
    print("  2. Medium  (1-100, 7 guesses)")
    print("  3. Hard    (1-200, 5 guesses)")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        return 1, 50, 10
    elif choice == "2":
        return 1, 100, 7
    elif choice == "3":
        return 1, 200, 5
    else:
        print("Invalid choice, defaulting to Medium.")
        return 1, 100, 7


def play_round():
    """Play a single round. Returns True if the player wants to play again."""
    low, high, max_guesses = get_difficulty()
    secret_number = random.randint(low, high)

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {max_guesses} guesses. Good luck!\n")

    attempts = 0
    guessed_correctly = False

    while attempts < max_guesses:
        remaining = max_guesses - attempts
        raw_value = input(f"Guess #{attempts + 1} (remaining: {remaining}): ").strip()

        if not raw_value.isdigit():
            print("Please enter a whole number.\n")
            continue

        guess = int(raw_value)
        attempts += 1

        if guess < low or guess > high:
            print(f"Stay within the range {low}-{high}!\n")
        elif guess < secret_number:
            print("Low!\n")
        elif guess > secret_number:
            print("High!\n")
        else:
            guessed_correctly = True
            print(f"\n Correct! The number was {secret_number}.")
            print(f"You got it in {attempts} attempt(s).\n")
            break

    if not guessed_correctly:
        print(f"\n Out of guesses! The number was {secret_number}.\n")

    play_again = input("Play again? (y/n): ").strip().lower()
    return play_again == "y"


def run_guessing_game():
    print("=" * 40)
    print("NUMBER GUESSING GAME")
    print("=" * 40)

    keep_playing = True
    while keep_playing:
        keep_playing = play_round()

    print("\nReturning to main menu...\n")


# SIMPLE CALCULATOR

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def get_number(prompt):
    """Keep asking until the user enters a valid number (int or float)."""
    while True:
        raw_value = input(prompt).strip()
        try:
            return float(raw_value)
        except ValueError:
            print("That's not a valid number. Try again.\n")


def format_result(value):
    """Print whole numbers without a trailing .0, keep decimals otherwise."""
    if value == int(value):
        return str(int(value))
    return f"{value:.4f}".rstrip("0").rstrip(".")


def run_calculator():
    print("=" * 40)
    print("SIMPLE CALCULATOR")
    print("=" * 40)

    while True:
        print("\n1. Add        (+)")
        print("2. Subtract   (-)")
        print("3. Multiply   (*)")
        print("4. Divide     (/)")
        print("5. Back to main menu")

        choice = input("Choose an operation (1-5): ").strip()

        if choice == "5":
            print("\nReturning to main menu...\n")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid option. Please choose a number from 1 to 5.\n")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == "1":
            result = add(num1, num2)
            symbol = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            symbol = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            symbol = "*"
        else:  # choice == "4"
            result = divide(num1, num2)
            symbol = "/"
            if result is None:
                print("\n Error: Cannot divide by zero.\n")
                continue

        print(f"\nResult: {format_result(num1)} {symbol} {format_result(num2)} = {format_result(result)}")



# MAIN MENU

def main():
    while True:
        print("\n" + "=" * 40)
        print("      WEEK 1 TASK")
        print("=" * 40)
        print("1. Number Guessing Game")
        print("2. Simple Calculator")
        print("3. Exit")
        print("=" * 40)

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            run_guessing_game()
        elif choice == "2":
            run_calculator()
        elif choice == "3":
            print("\nGoodbye! 👋")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()