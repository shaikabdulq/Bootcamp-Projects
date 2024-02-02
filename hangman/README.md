
# Hangman Game

## Overview
This project implements a classic game of Hangman. The game randomly selects a movie name, and the player attempts to guess it by suggesting letters within a certain number of guesses.

## Files Description
- `hangman.py`: Main script for running the Hangman game. It includes the game logic and user interaction.
- `list.py`: Contains the list of movie names from which the Hangman game chooses a random one.
- `art.py`: Provides ASCII art for the hangman graphics displayed during the game.

## How to Play
1. Run `hangman.py`.
2. The game will display a series of blanks representing the letters of a random word.
3. Guess letters one at a time. If the letter is in the word, the game fills it in all the correct positions.
4. If the letter is not in the word, a part of the hangman is drawn (a chance is lost).
5. The game continues until either the word is fully guessed or the hangman is completely drawn (all chances are lost).

## Requirements
- Python 3.11
