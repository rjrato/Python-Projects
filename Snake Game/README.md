# Snake Game

A classic Snake game implemented in Python using the Turtle module.

## Overview

This Python program simulates the classic Snake game where the player controls a snake to eat food items and grow in length. The game ends if the snake runs into a wall or into itself.

## Features

- **Snake Movement**: 
  - Use arrow keys ('Up', 'Down', 'Left', 'Right') to change the snake's direction.
  - The snake moves continuously in the current direction until a key is pressed to change direction or the game ends.

- **Food Generation**: 
  - Food appears randomly on the screen after the snake eats the current piece.
  - Each time the snake eats food, it grows longer and the player scores points.

- **Collision Detection**: 
  - Detects collisions with walls and resets the game if the snake hits a boundary.
  - Detects collisions with the snake's own body, ending the game if the snake runs into itself.

## Installation

Ensure you have Python installed on your system. Clone the repository and run the following command:

```bash
python main.py
```

## Dependencies
- Python 3.x
- Turtle graphics library (typically included in standard Python installations)
