# Python CLI Toolkit — Number Guessing Game & Calculator

A beginner-friendly command-line application built with core Python, combining two classic mini-projects into one interactive menu: a "Number Guessing Game" and a "Simple Calculator".

This project was built as part of a Week 1 "Python Basics & Control Flow" learning track, focused on translating fundamental concepts into a working, real-world CLI tool.

# Features

# Number Guessing Game
- Three difficulty levels (Easy, Medium, Hard) with different number ranges and guess limits
- Randomized target number using Python's `random` module
- Real-time feedback (too high / too low) after every guess
- Input validation to reject non-numeric input
- Replay option after each round

# Simple Calculator
- Supports addition, subtraction, multiplication, and division
- Menu-driven interface for selecting operations
- Handles division-by-zero gracefully
- Validates numeric input (accepts both integers and decimals)
- Clean output formatting (no unnecessary trailing decimals)

Both tools run from a single unified main menu, so the user can freely switch between the game and the calculator without restarting the program.

## Future Improvements
- Add a "best score" / leaderboard tracker for the guessing game
- Support additional calculator operations (exponents, square root, modulo)
- Add unit tests for core functions
- Package as an installable CLI command

## License
This project is open source and available for personal or educational use.
