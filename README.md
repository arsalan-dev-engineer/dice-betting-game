# Roll to Target Game

## Overview
Roll to Target is an interactive dice-based game where the objective is to reach or exceed a randomly assigned target score by managing your bets and rolling dice. Players start with a balance and must place bets before each round to either win or lose based on dice rolls. The game includes a bonus round for added excitement.

## Features
- **Dice Rolls**: Players roll a dice to determine the outcome of each bet.
  - Rolls 1 or 2: Lose your bet.
  - Rolls 3 or 4: Win 1.5x your bet.
  - Roll 5: Win 2x your bet.
  - Roll 6: Enter the bonus round.
- **Bonus Round**: If you roll a 6, you get a bonus roll that can either result in a loss or a 3x win.
- **Game Stats**: Track your total games played, won, lost, and your highest balance achieved.

## Requirements
- Python 3.x
- `rich` library for colorful terminal output (install via `pip install rich`)

## How to Play
1. Run the script.
2. Select an option from the main menu:
   - Read the rules.
   - Start a new game.
   - Check game stats.
   - Quit the game.
3. In each round, place your bet, roll the dice, and try to reach your target score while managing your balance.

## Game Rules
- The game ends when your balance reaches zero (you lose) or when you reach or exceed the target score (you win).
- Winnings and losses are automatically calculated after each round.

## Installation
Clone this repository:
```bash
https://github.com/arsalan-dev-engineer/dice-betting-game.git
```
