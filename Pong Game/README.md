# Pong Game

A simple implementation of the classic Pong game using Python's Turtle module.

## Overview

This Python program creates a two-player Pong game where each player controls a paddle to hit a ball back and forth across the screen. The game ends when one player misses the ball, allowing the opponent to score a point.

## Features

- **Player Controls**: 
  - Left Player: Moves with 'W' (up) and 'S' (down) keys.
  - Right Player: Moves with 'Up Arrow' (up) and 'Down Arrow' (down) keys.

- **Scoring**: 
  - Scores are displayed for both players on the screen.
  - Game resets after each point with paddles and ball returning to starting positions.

- **Ball Movement**: 
  - The ball moves at variable speeds, increasing after each paddle collision.
  - It bounces off walls and paddles, changing direction accordingly.

## Installation

To run the game, ensure you have Python installed on your system. Clone the repository and execute the following command:

```bash
python main.py
```
## Dependencies
- Python 3.x
- Turtle graphics library (usually included in standard Python installations)
